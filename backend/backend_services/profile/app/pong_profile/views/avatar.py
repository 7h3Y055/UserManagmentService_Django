from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from dotmap import DotMap
import logging, os, jwt, requests
from django.conf import settings
import json

# profile/avatar              (POST)      : upload new avatar
# profile/avatar              (DELETE)    : remove avatar (set to default)





def get_user(req):
    try:
        res = requests.get('http://localhost:8000/account/whoami/', headers={'Authorization': req.headers.get('Authorization')})
        if res.status_code != 200:
            raise
        return DotMap(res.json())
    except:
        logging.error('Invalid token')
    return None


def save_user(req, user: DotMap):
    user = json.dumps(user.toDict())
    try:
        res = requests.patch(
            'http://localhost:8000/account/update-profile/', 
            user,
            headers={'Authorization': req.headers.get('Authorization')})
        if res.status_code != 200:
            print(res.status_code)
            raise
        return res.json()
    except:
        logging.error('Invalid token')
    return None



from django.http import JsonResponse


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def avatar(req):    
    user = get_user(req)
    if not user:
        return JsonResponse({'error': 'unauthenticated'}, status=401)
    
    
    
    
    user = save_user(req, user)
    if not user:
        return JsonResponse({'error': '2'}, status=400)
    
    return Response(user, status=200)
    











def remove_old_avatar(username):
    extensions = ['.jpg', '.png', '.gif', '.webp']
    for ext in extensions:
        try:
            os.remove(os.environ.get('PROFILE_IMAGE_PATH') + username.replace(' ', '_') + ext)
            break
        except FileNotFoundError:
            continue




@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def avatara(req):
    
    payload = get_user(req.headers['Authorization'].split(' ')[1])
    
    if not payload:
        return Response({'error': 'Invalid token'}, status=400)
    
    print(payload)
    
    return Response({'cccccc': 'AAAAAAAAAAAAAAAAAA'}, status=200)
    
    if req.method == 'POST':
        logging.info(f'Uploading new avatar {req.user.username}')
        extensions = {
            'image/jpeg': '.jpg',
            'image/png': '.png',
            'image/gif': '.gif',
            'image/webp': '.webp',
        }
        extension = extensions.get(req.headers['Content-Type'])
        if not extension:
            logging.error('Invalid image type')
            return Response({'error': 'Invalid image type'}, status=400)
        path = os.environ.get('PROFILE_IMAGE_PATH') + req.user.username.replace(' ', '_') + extension
        remove_old_avatar(req.user.username)
        file = open(path, 'wb')
        file.write(req.body)
        file.close()
        req.user.avatar_url = os.environ.get('DOMAIN') + '/' + path
        req.user.save()
        res = Response(status=201)
        res.headers['Location'] = req.user.avatar_url
        return res
    elif req.method == 'DELETE':
        logging.info('Removing avatar')
        print(os.environ.get('PROFILE_IMAGE_PATH') + req.user.avatar_url.split('/')[-1])
        if req.user.avatar_url == os.environ.get('PROFILE_IMAGE_PATH') + os.environ.get('DEFAULT_IMAGE'):
            logging.error('User does not have an avatar')
            return Response({'error': 'User does not have an avatar'}, status=400)
        try:
            os.remove(os.environ.get('PROFILE_IMAGE_PATH') + req.user.avatar_url.split('/')[-1])
        except:
            logging.error('Tried to remove avatar that does not exist')
            return Response({'error': 'Tried to remove avatar that does not exist'}, status=500)
        req.user.avatar_url = os.environ.get('DOMAIN') + '/' + os.environ.get('PROFILE_IMAGE_PATH') + os.environ.get('DEFAULT_IMAGE')
        req.user.save()
        return Response(status=204)



