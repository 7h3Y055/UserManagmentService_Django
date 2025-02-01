from django.http import JsonResponse, HttpResponse
from ..models import Player, Friendship
from .serializer import UserSerializer
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt # just for testing
# def unfriend(req, user_id):
#     if not req.user.is_authenticated:
#         return JsonResponse({'error': 'Unauthorized'}, status=401)
#     if req.method == 'DELETE':
#         try:
#             fs = Friendship.objects.get(sender_id=req.user.id, received_id=user_id, status='FR')
#             fs.delete()
#             return HttpResponse(status=204)
#         except:
#             try:
#                 fs = Friendship.objects.get(sender_id=user_id, received_id=req.user.id, status='FR')
#                 fs.delete()
#                 return HttpResponse(status=204)
#             except:
#                 return JsonResponse({'error': 'you are not friends'}, status=400)
#     return HttpResponse(status=405)