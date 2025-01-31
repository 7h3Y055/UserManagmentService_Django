from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import UserSerializer
import json



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def whoami(req):
    return Response(UserSerializer(req.user).data, status=200)




@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(req):
    try:
        body_unicode = req.body.decode('utf-8')
        json_body = json.loads(body_unicode)
        serializer = UserSerializer(req.user, data=json_body, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON'}, status=400)

