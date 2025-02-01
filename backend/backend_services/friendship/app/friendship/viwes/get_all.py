from django.http import JsonResponse, HttpResponse
from ..models import Friendship
from django.db.models import Q
# from .serializer import UserSerializer

# RELISHIONS = {
#     'blocked': 'BL',
#     'pending': 'PN',
#     'friends': 'FR',
#     'all': '*',
# }

# STATUS = {
#     'online': 'ON',
#     'offline': 'OF',
#     'in-game': 'IG'
# }


# def ft_filter(fs, id, status):
#     for i in fs:
#         if i.sender_id != id:
#             id = i.sender_id
#         else:            
#             id = i.received_id
#         fr = Player.objects.filter(id=id)
        
#         if not (fr.count() == 1 and fr[0].status == status):
#             fs = fs.exclude(id=i.id)

#     return fs


# def get_friends(req):
#     if not req.user.is_authenticated:
#         return JsonResponse({'error': 'Unauthorized'}, status=401)
#     if req.method != 'GET':
#         return HttpResponse(status=405)
    
#     status = req.GET.get('status', 'all')
#     try:
#         limit = min(int(req.GET.get('limit', 10), 100))
#         offset = int(req.GET.get('offset', 0))
#         if limit < 0 or offset < 0:
#             raise
#     except:
#         return JsonResponse({'error':'invalid value in \'limit\' and/or \'offset\''}, status=400)
        
#     try:
#         if status in RELISHIONS:
#             if status != 'all':
#                 fr = Friendship.objects.filter((Q(sender_id=req.user.id) | Q(received_id=req.user.id)) & Q(status=RELISHIONS[status]))
#             elif status == 'all':
#                 fr = Friendship.objects.filter(Q(sender_id=req.user.id) | Q(received_id=req.user.id))
#         elif status in STATUS:
#             fr = Friendship.objects.filter((Q(sender_id=req.user.id) | Q(received_id=req.user.id)) & Q(status='FR'))
#             fr = ft_filter(fr, req.user.id, STATUS[status])
#         else:
#             return JsonResponse({'error':'invalid value in \'status\''}, status=400)
#         fr_ids = []
#         for i in fr.values_list('received_id', 'sender_id'):
#             if i[0] == req.user.id:
#                 fr_ids += [i[1]]
#             elif i[1] == req.user.id:
#                 fr_ids += [i[0]]
#         fr = Player.objects.filter(id__in=fr_ids)
#     except Player.DoesNotExist:
#         return JsonResponse({'error':'no friends'}, status=404)
    
#     serialized = UserSerializer(fr[offset:offset+limit], context={'user': req.user}, many=True)
#     return JsonResponse({'friends':serialized.data}, status=200)

