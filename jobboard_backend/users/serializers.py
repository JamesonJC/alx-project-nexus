from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
import logging
logger = logging.getLogger(__name__)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        try:
            validated_data.pop('password2')
            username = validated_data.get('username')
            email = validated_data.get('email')
            password = validated_data.get('password')

            if not all([username, email, password]):
                raise serializers.ValidationError("Missing required fields.")

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return user
        except Exception as e:
            logger.error(f"Registration error: {e}")
            raise serializers.ValidationError(f"Registration failed: {str(e)}")