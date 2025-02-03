from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import UserSerializer
from ..models import Player
import json

# /account/users/n?=3&sort=newest    (GET)     : get top 'n' of users sorted by 'sort'

def check_query_params(req):
    n = req.query_params.get('n', 0)
    try:
        n = int(n)
        if n < 1 or n > 10:
            raise ValueError
    except ValueError:
        raise ValueError('n must be an integer between 1 and 10')
        
    sorts = ['newest', 'oldest']
    sort = req.query_params.get('sort', '')
    if sort not in sorts:
        raise ValueError(f'sort must be either {sorts}')
    return n, sort


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(req):
    try:
        n, sort = check_query_params(req)
    except ValueError as e:
        return Response({'error': str(e)}, status=400)
    
    if sort == 'newest':
        users = Player.objects.order_by('-created_at')[:n]
    elif sort == 'oldest':
        users = Player.objects.order_by('created_at')[:n]
    users = UserSerializer(users, many=True)
    return Response(users.data, status=200)
