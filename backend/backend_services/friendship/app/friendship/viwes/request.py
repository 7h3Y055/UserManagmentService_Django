
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from ..models import Friendship
from django.db.models import Q
from .user import get_user


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def send_friend_request(req, user_id):
    if req.method == 'POST': # POST
        user = get_user(req, user_id)
        if not user:
            return Response({'error':'this user not found'})
        if (user.id == req.user.id):
            return Response({'error':'you can\'t send request to your self'})
        fs = Friendship.objects.filter((Q(sender_id=req.user.id) | Q(sender_id=user.id)) & (Q(received_id=user.id) | Q(received_id=req.user.id)))
        if fs.filter(status='BL').count():
            return Response({'error':'you can\'t send request to this user'})
        else:
            if fs.filter(status='FR').count():
                return Response({'success':'you are already friends'}, status=200)
            elif fs.filter(status='PN').count():
                return Response({'success':'you are already send request to this user'}, status=200)
            else:
                Friendship.objects.create(sender_id=req.user.id, received_id=user.id)
                return Response({'success':f'request sended successfully to {user.username}'}, status=200)
    elif req.method == 'DELETE':
        fs = Friendship.objects.filter((Q(sender_id=req.user.id) | Q(sender_id=user_id)) & (Q(received_id=user_id) | Q(received_id=req.user.id)))
        if fs.filter(status='PN').count():
            fs.delete()
            return Response(status=204)
        else:
            return Response({'error':'this request dosen\'t exist'}, status=400)
    return Response(status=405)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_request(req, user_id):
    try:
        fs = Friendship.objects.get(sender_id=user_id, received_id=req.user.id, status='PN')
        fs.status = 'FR' # ('FR','friends'),
        fs.save()
        return Response({'success':'accepted'}, status=200)
    except Friendship.DoesNotExist:
        return Response({'error':'this request dosen\'t exist'}, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reject_request(req, user_id):
    try:
        fs = Friendship.objects.get(received_id=req.user.id, sender_id=user_id, status='PN')
        fs.delete()
        return Response({'success':'rejected'}, status=200)
    except:
        return Response({'error':'this request dosen\'t exist'}, status=400)
