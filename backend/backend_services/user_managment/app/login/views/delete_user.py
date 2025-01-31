from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import logging

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(req):
    req.user.delete()
    logging.info(f'Delete user {req.user.email}')
    return Response(status=204)
