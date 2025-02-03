from ..models import Friendship
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .user import get_user
import json

RELISHIONS = {
    'blocked': 'BL',
    'pending': 'PN',
    'friends': 'FR',
    'all': '*',
}

STATUS = {
    'online': 'ON',
    'offline': 'OF',
    'in-game': 'IG'
}


def ft_filter(fs, id, status, req):
    for i in fs:
        if i.sender_id != id:
            id = i.sender_id
        else:            
            id = i.received_id
        fr = get_user(req, id)
        
        if not (fr.count() == 1 and fr[0].status == status):
            fs = fs.exclude(id=i.id)

    return fs

def get_relation(id1, id2):
    return 'FR'
    # try:
    #     fs = Friendship.objects.filter(
    #         Q(sender_id=id1, received_id=id2) | 
    #         Q(sender_id=id2, received_id=id1)
    #     )
    #     if fs.count() == 0:
    #         return None
    #     elif fs.count() == 1:
    #         return fs[0].status
    #     else:
    #         return 'BL'
    # except:
    #     return str('Error')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_friends(req):
    status = req.GET.get('status', 'all')
    try:
        limit = min( int(req.GET.get('limit', 10)), 100)
        offset = int(req.GET.get('offset', 0))
        if limit < 0 or offset < 0:
            raise
    except Exception as e:
        return Response({'error':'invalid value in \'limit\' and/or \'offset\''}, status=400)
        
    if status in RELISHIONS:
        if status != 'all':
            fr = Friendship.objects.filter((Q(sender_id=req.user.id) | Q(received_id=req.user.id)) & Q(status=RELISHIONS[status]))
        elif status == 'all':
            fr = Friendship.objects.filter(Q(sender_id=req.user.id) | Q(received_id=req.user.id))
    elif status in STATUS:
        fr = Friendship.objects.filter((Q(sender_id=req.user.id) | Q(received_id=req.user.id)) & Q(status='FR'))
        fr = ft_filter(fr, req.user.id, STATUS[status], req)
    else:
        return Response({'error':'invalid value in \'status\''}, status=400)
    fr_ids = []
    for i in fr.values_list('received_id', 'sender_id'):
        if i[0] == req.user.id:
            fr_ids += [i[1]]
        elif i[1] == req.user.id:
            fr_ids += [i[0]]
    fr_ids = fr_ids[offset:offset+limit]
    fr_ids = [1, 2]
    
    
    friends_list = []
    for i in fr_ids:
        user = get_user(req, i)
        if user:
            friends_list.append(user.toDict())
            friends_list[-1]['relation'] = get_relation(req.user.id, i)
    
    result = json.dumps({'friends': friends_list})
    # print(friends_list)

    return Response(json.loads(result), status=200)

