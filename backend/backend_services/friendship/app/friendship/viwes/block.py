from ..models import Friendship
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .user import get_user

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def block_request(req, user_id):
    if not req.user.is_authenticated:
        return Response({'error': 'Unauthorized'}, status=401)
    if req.method == 'POST': # POST
        try:
            user = get_user(req, user_id)
            if not user:
                raise Exception('user not found')
            if req.user.id == user.id:
                return Response({'error':'you can\'t block your self'}, status=400)
            try:
                fs = Friendship.objects.get(sender_id=req.user.id, received_id=user_id, status='BL')
                return Response({'seccess':'already blocked'}, status=200)
            except:
                Friendship.objects.create(sender_id=req.user.id, received_id=user.id, status='BL') # ('BL','blocked'),
                return Response({'seccess':'blocked'}, status=200)
        except:
            return Response({'error':'user not found'}, status=400)
    elif req.method == 'DELETE': # DELETE
        try:
            fs = Friendship.objects.get(sender_id=req.user.id, received_id=user_id, status='BL')
            fs.delete()
            return Response(status=204)
        except:
            return Response({'error':'this user is not blocked'}, status=400)
    return Response(status=405)