from rest_framework import serializers
from ..models import Player

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'avatar_url', 'status', 'created_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'avatar_url': {'read_only': True},
            'two_FA': {'read_only': True},
            'created_at': {'read_only': True},
        }

    def validate_username(self, value):
        return self.validate_name(value, 'Username')

    def validate_first_name(self, value):
        return self.validate_name(value, 'First name')
    
    def validate_last_name(self, value):
        return self.validate_name(value, 'Last name')

    def validate_name(self, value, type):
        if len(value) < 3:
            raise serializers.ValidationError(f"{type} too short")
        if len(value) > 30:
            raise serializers.ValidationError(f"{type} too long")
        for c in value:
            if not (c.isalnum() or c == '_' or c == '-'):
                raise serializers.ValidationError(f"{type} should only contain letters, numbers, underscores, and hyphens")
        return value


