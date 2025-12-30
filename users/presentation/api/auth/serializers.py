from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    # password_confirm = serializers.CharField(max_length=100) # Optional complexity, skipping for strict Hexagonal simplicity unless requested

    # Simplified for now to match UseCase exactly
