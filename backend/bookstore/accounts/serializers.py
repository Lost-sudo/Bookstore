from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from rest_framework.validators import UniqueValidator

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all()), validate_email],
    )

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'password2', 'is_seller']

        def validate(self, data):
            if data['password'] != data['password2']:
                raise serializers.ValidationError({"password": "Passwords do not match"})
            return data
        
        def create(self, validated_data):
            validated_data.pop('password2')
            user = User.objects.create_user(
                email=validated_data['email'],
                full_name=validated_data['full_name'],
                password=validated_data['password'],
                is_seller=validated_data('is_seller', False)
            )
            return user
