from rest_framework import serializers
from ..models import Friendship
from django.db.models import Q

# class UserSerializer(serializers.ModelSerializer):
    
#     relation = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Player
#         fields = ['id', 'username', 'first_name', 'last_name', 'avatar_url', 'status', 'relation']
#         extra_kwargs = {
#             'id': {'read_only': True},
#         }
    
#     def get_relation(self, obj):
#         try:
#             fs = Friendship.objects.filter(
#                 Q(sender_id=self.context['user'].id, received_id=obj.id) | 
#                 Q(sender_id=obj.id, received_id=self.context['user'].id)
#             )
#             if fs.count() == 0:
#                 return None
#             elif fs.count() == 1:
#                 return fs[0].status
#             else:
#                 return 'BL'
#         except:
#             return str('Error')
