from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializer import UserSerializer
from ..models import Player
from rest_framework.response import Response
from django.db.models import Q


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(req):
    q = req.GET.get('q', '').strip()
    if not q:
        return Response({
            'error': 'Invalid parameters',
            'details': 'Please provide valid \'q\''
        }, status=400)
    try:
        limit = min(int( req.GET.get('limit', 10) ) , 100)
        offset = int(req.GET.get('offset', 0))

        if limit < 0 or offset < 0:
            raise ValueError
    except ValueError:
        return Response({'error':'invalid value in \'limit\' and/or \'offset\''}, status=400)
    

    sp = q.split(' ')
    result = Player.objects.filter(Q(username__icontains=q) | ( Q(first_name__icontains=sp[0]) & Q(last_name__icontains=' '.join(sp[1:]))))

    serialized = UserSerializer(result[offset:offset+limit], context={'user': req.user}, many=True)
    return Response({'result': serialized.data}, status=200)
