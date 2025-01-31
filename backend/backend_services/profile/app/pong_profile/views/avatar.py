from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import logging, os
from .geter_seter import *

# profile/avatar              (POST)      : upload new avatar
# profile/avatar              (DELETE)    : remove avatar (set to default)




def remove_old_avatar(username):
    extensions = ['.jpg', '.png', '.gif', '.webp']
    for ext in extensions:
        try:
            os.remove(os.environ.get('PROFILE_IMAGE_PATH') + username.replace(' ', '_') + ext)
            break
        except FileNotFoundError:
            continue


    



@api_view(['POST', 'DELETE'])
# @permission_classes([IsAuthenticated])
def avatara(req):    
    user = get_user(req)
    if not user:
        return Response({'error': 'unauthenticated'}, status=401)
    
    return Response(user.toDict(), status=200)

@api_view(['POST', 'DELETE'])
# @permission_classes([IsAuthenticated])
def avatar(req):
    user = get_user(req)
    if not user:
        return Response({'error': 'unauthenticated'}, status=401)
    
    if req.method == 'POST':
        logging.info(f'Uploading new avatar {user.username}')
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
        path = os.environ.get('PROFILE_IMAGE_PATH') + user.username.replace(' ', '_') + extension
        remove_old_avatar(user.username)
        file = open(path, 'wb')
        file.write(req.body)
        file.close()
        user.avatar_url = os.environ.get('DOMAIN') + '/' + path
        user = save_user(req, user)
        if not user:
            logging.error('Failed to save user')
            return Response({'error': 'Failed to save user'}, status=400)
        # user.save()
        res = Response(status=201)
        res.headers['Location'] = user.avatar_url
        return res
    elif req.method == 'DELETE':
        logging.info('Removing avatar')
        print(os.environ.get('PROFILE_IMAGE_PATH') + user.avatar_url.split('/')[-1])
        if user.avatar_url == os.environ.get('PROFILE_IMAGE_PATH') + os.environ.get('DEFAULT_IMAGE'):
            logging.error('User does not have an avatar')
            return Response({'error': 'User does not have an avatar'}, status=400)
        try:
            os.remove(os.environ.get('PROFILE_IMAGE_PATH') + user.avatar_url.split('/')[-1])
        except:
            logging.error('Tried to remove avatar that does not exist')
            return Response({'error': 'Tried to remove avatar that does not exist'}, status=500)
        user.avatar_url = os.environ.get('DOMAIN') + '/' + os.environ.get('PROFILE_IMAGE_PATH') + os.environ.get('DEFAULT_IMAGE')
        user = save_user(req, user)
        if not user:
            logging.error('Failed to save user')
            return Response({'error': 'Failed to save user'}, status=400)
        # user.save()
        return Response(status=204)



