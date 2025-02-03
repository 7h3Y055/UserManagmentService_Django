from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser
import requests, json, logging


def get_user(auth: str):
    res = requests.get('http://localhost:8000/account/whoami/', headers={'Authorization': 'Bearer ' + str(auth)})
    if res.status_code != 200:
        return None
    return res.json()

class MockPlayer:
    auth = None
    
    def __init__(self, validated_token):
        MockPlayer.auth = validated_token
        user = get_user(validated_token)
        if not user:
            self.is_authenticated = False
            return

        self.id = user.get('id')
        self.username = user.get('username')
        self.first_name = user.get('first_name')
        self.last_name = user.get('last_name')
        self.bio = user.get('bio')
        self.avatar_url = user.get('avatar_url')
        self.status = user.get('status')
        self.created_at = user.get('created_at')
        self.is_authenticated = True

    def save(self):
        user = json.dumps(self.__dict__)
        
        try:
            res = requests.patch(
                'http://localhost:8000/account/update-profile/', 
                user,
                headers={'Authorization': 'Bearer ' + str(self.auth)})
            if res.status_code != 200:
                raise
            return res.json()
        except:
            logging.error('Invalid token')
        return None

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get('user_id')

        if not user_id:
            return AnonymousUser()

        return MockPlayer(validated_token)
