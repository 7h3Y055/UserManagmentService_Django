from django.http import JsonResponse, HttpResponse
from ..models import Player, Friendship
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt # just for testing
# def block_request(req, user_id):
#     if not req.user.is_authenticated:
#         return JsonResponse({'error': 'Unauthorized'}, status=401)
#     if req.method == 'POST': # POST
#         try:
#             user = Player.objects.get(id=user_id)
#             if req.user.id == user.id:
#                 return JsonResponse({'error':'you can\'t block your self'}, status=400)
#             try:
#                 fs = Friendship.objects.get(sender_id=req.user.id, received_id=user_id, status='BL')
#                 return JsonResponse({'seccess':'already blocked'}, status=200)
#             except:
#                 Friendship.objects.create(sender_id=req.user.id, received_id=user.id, status='BL') # ('BL','blocked'),
#                 return JsonResponse({'seccess':'blocked'}, status=200)
#         except:
#             return JsonResponse({'error':'user not found'}, status=400)
#     elif req.method == 'DELETE': # DELETE
#         try:
#             fs = Friendship.objects.get(sender_id=req.user.id, received_id=user_id, status='BL')
#             fs.delete()
#             return HttpResponse(status=204)
#         except:
#             return JsonResponse({'error':'this user is not blocked'}, status=400)
#     return HttpResponse(status=405)