from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, HttpResponse
import logging, os

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
@permission_classes([IsAuthenticated])
def avatar(req):
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
            return JsonResponse({'error': 'Invalid image type'}, status=400)
        path = os.environ.get('PROFILE_IMAGE_PATH') + req.user.username.replace(' ', '_') + extension
        remove_old_avatar(req.user.username)
        file = open(path, 'wb')
        file.write(req.body)
        file.close()
        req.user.avatar_url = os.environ.get('DOMAIN') + '/' + path
        req.user.save()
        res = HttpResponse(status=201)
        res.headers['Location'] = req.user.avatar_url
        return res
    
    if req.method == 'DELETE':
        logging.info('Removing avatar')
        if req.user.avatar_url == os.environ.get('PROFILE_IMAGE_PATH') + os.environ.get('DEFAULT_IMAGE'):
            logging.error('User does not have an avatar')
            return JsonResponse({'error': 'User does not have an avatar'}, status=400)
        try:
            os.remove(os.environ.get('PROFILE_IMAGE_PATH') + req.user.avatar_url.split('/')[-1])
        except:
            logging.error('Tried to remove avatar that does not exist')
            return JsonResponse({'error': 'Tried to remove avatar that does not exist'}, status=500)
        req.user.avatar_url = os.environ.get('DOMAIN') + '/' + os.environ.get('PROFILE_IMAGE_PATH') + os.environ.get('DEFAULT_IMAGE')
        req.user.save()
        return HttpResponse(status=204)
    return HttpResponse(status=405)



