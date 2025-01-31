from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        try:
            return super().get_validated_token(raw_token)
        except Exception as e:
            raise AuthenticationFailed('Invalid token') from e


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(req):
    logging.info(f'User {req.user.email} logged out')
    try:
        refresh_token = req.data.get('refresh')
        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=400)

        token = RefreshToken(refresh_token)
        token.blacklist()
        res = Response({"message": "Logged out successfully"}, status=200)
        return res
    except Exception as e:
        return Response({"error": str(e)}, status=400)