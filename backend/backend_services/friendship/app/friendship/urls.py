from django.urls import path
from .viwes import *


urlpatterns = [
        path('<int:user_id>/request', send_friend_request),
        # path('<int:user_id>/request/accept', accept_request),
        # path('<int:user_id>/request/reject', reject_request),
        # path('<int:user_id>/block', block_request),
        # path('<int:user_id>/friend', unfriend),
        # path('', get_friends),
        # path('notification', ),
        # path('notification/{id}', ),
        
        # path('search', search),
        # path('<int:user_id>', info),
]
