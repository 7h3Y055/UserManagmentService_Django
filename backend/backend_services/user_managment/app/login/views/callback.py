from ..models import Player
from django.contrib.auth import login
from .serializer import UserSerializer
import requests, os, logging
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
from restframework.response import Response
from restframework.decorators import api_view, permission_classes
from restframework.permissions import AllowAny


def get_oauth2_urls(provider):
    if provider == '42':
        return {
            'token_url': 'https://api.intra.42.fr/oauth/token',
            'userinfo_url': 'https://api.intra.42.fr/v2/me',
            'client_id': os.environ.get('SOCIAL_AUTH_42_OAUTH2_KEY'),
            'client_secret': os.environ.get('SOCIAL_AUTH_42_OAUTH2_SECRET'),
        }
    elif provider == 'google':
        return {
            'token_url': 'https://oauth2.googleapis.com/token',
            'userinfo_url': 'https://www.googleapis.com/oauth2/v1/userinfo',
            'client_id': os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'),
            'client_secret': os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
        }
    else:
        raise ValueError('Invalid OAuth2 provider')


def image_url(image_url, username):
    extensions = {
        'image/jpeg': '.jpg',
        'image/png': '.png',
        'image/gif': '.gif',
        'image/webp': '.webp',
    }
    try:
        req = requests.get(image_url)
        if req.status_code != 200:
            raise
        if not extensions.get(req.headers['Content-Type']):
            raise
        path = os.environ.get('PROFILE_IMAGE_PATH') + username.replace(' ', '_') + extensions.get(req.headers['Content-Type'])
        file = open(path, 'wb')
        file.write(req.content)
    except : # default
        path = os.environ.get('PROFILE_IMAGE_PATH') + 'default.jpg'
    return os.environ.get('DOMAIN') + '/' + path


def create_user(user_info, provider):
    if provider == '42':
        user = Player.objects.create_user(
            username=user_info['login'].replace(' ', '_'),
            email=user_info['email'],
            first_name=user_info['first_name'],
            last_name=user_info['last_name'],
            avatar_url=image_url(user_info['image']['versions']['small'], user_info['login'])
        )
    else:  # google
        user = Player.objects.create_user(
            username=user_info['name'].replace(' ', '_'),
            email=user_info['email'],
            first_name=user_info['given_name'],
            last_name=user_info['family_name'],
            avatar_url=image_url(user_info['picture'], user_info['name'])
        )
    return user

@api_view(['GET'])
@permission_classes([AllowAny])
def callback(req):
    if req.COOKIES.get('state') != req.GET.get('state'):
        logging.error('Invalid state, The state parameter does not match')
        return Response({'error': 'Invalid state',
                         'error_description': 'The state parameter does not match'}, status=400)
    
    code = req.GET.get('code')
    if not code:
        logging.error('No code provided')
        return Response({'error': 'No code provided',
                         'error_description': 'Authorization code is missing from the request'}, status=400)
    
    try:
        oauth2_urls = get_oauth2_urls(req.COOKIES.get('oauth2_provider'))
    except ValueError:
        logging.error('Invalid OAuth2 provider')
        return Response({'error': 'Invalid OAuth2 provider',
                         'error_description': 'The OAuth2 provider is not set in the cookie or it has been edited'}, status=400)
    
    
    if req.GET.get('error'):
        logging.error(f"Error: {req.GET.get('error')}, Description: {req.GET.get('error_description')}")
        return Response({'error': req.GET.get('error'),
                         'error_description': req.GET.get('error_description')}, status=400)

    body = {
        "grant_type": "authorization_code",
        "client_id": oauth2_urls['client_id'],
        "client_secret": oauth2_urls['client_secret'],
        'code': code,
        "redirect_uri": str(os.environ.get('SOCIAL_AUTH_REDIRECT_URI'))',
    }

    response = requests.post(url=oauth2_urls['token_url'], data=body)

    if response.status_code != 200:
        logging.error(f"Failed to obtain token: {response.json().get('error')}, Description: {response.json().get('error_description')}")
        return Response({'error': response.json().get('error'), 'error_description': response.json().get('error_description')}, status=response.status_code)
    
    access_token = response.json().get('access_token')
    if not access_token:
        logging.error('No access token provided')
        return Response({'error': 'No access token provided',
        'error_description': 'The access token is missing from the token response'}, status=400)
        
    response = requests.get(url=oauth2_urls['userinfo_url'], headers={'Authorization': f'Bearer {access_token}'})
    if response.status_code != 200:
        logging.error('Failed to obtain user info')
        return Response({'error': 'Failed to obtain user info',
        'error_description': response.json().get('error_description')}, status=response.status_code)
    
    user_info = response.json()
    
    try:
        user = Player.objects.get(email=user_info['email'])
    except Player.DoesNotExist:
        logging.info(f'creating new User {user_info["email"]} does not exist')
        user = create_user(user_info, req.COOKIES.get('oauth2_provider'))
    
    
    # Generate JWT tokens
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)
    
    logging.info(f'login in User {user_info["email"]}')
    res = Response({
        'access_token': access_token,
        'refresh_token': refresh_token
    }, status=201)
    
    res.delete_cookie('state')
    
    return res
