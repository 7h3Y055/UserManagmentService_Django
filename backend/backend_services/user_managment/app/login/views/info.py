from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from ..models import Player
from .serializer import UserSerializer
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def info(req, user_id):
    try:
        user = Player.objects.get(id=user_id)
        return Response(UserSerializer(user, context={'user': req.user}).data, status=200)
    except:
        return Response({'error': 'user not found'}, status=400)

