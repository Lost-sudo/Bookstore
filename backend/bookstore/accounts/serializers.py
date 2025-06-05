from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from rest_framework.validators import UniqueValidator
from .models import Profile, SellerProfile

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)
    phone_number = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all()), validate_email],
    )

    class Meta:
        model = User
        fields = ['email', 'full_name', 'phone_number', 'password', 'password2']


    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data
        
    def create(self, validated_data):
        print("Validated data: ", validated_data)
        validated_data.pop('password2')
        user = User.objects.create_user(
        email=validated_data['email'],
        full_name=validated_data['full_name'],
        phone_number=validated_data['phone_number'],
        password=validated_data['password'],
        is_seller = False
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    shipping_address = serializers.CharField()
    payment_card = serializers.CharField()

    class Meta:
        model = Profile
        fields = ['profile_picture', 'shipping_address', 'payment_card']

    def create(self, validated_data):
        profile = Profile.objects.create(
            user = self.context['request'].user,
            profile_picture = validated_data.get('profile_picture'), #TODO: add image upload handle
            shipping_address = validated_data['shipping_address'],
            payment_card = validated_data['payment_card']
        )
        return profile

    def update(self, instance, validated_data):
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.shipping_address = validated_data.get('shipping_address', instance.shipping_address)
        instance.payment_card = validated_data.get('payment_card', instance.payment_card)
        instance.save()
        return instance

class SellerProfileSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField()
    shop_description = serializers.CharField()
    shop_address = serializers.CharField()

    class Meta:
        model = SellerProfile
        fields = ['shop_name', 'shop_description', 'shop_address']

    def create(self, validated_data):
        seller_profile = SellerProfile.objects.create(
            user = self.context['request'].user,
            shop_name = validated_data['shop_name'],
            shop_description = validated_data['shop_description'],
            shop_address = validated_data['shop_address'],
            shop_logo = validated_data.get('shop_logo'), #TODO: add image upload handle
            banner = validated_data.get('banner') #TODO: add image upload handle
        )
        return seller_profile
    
    def update(self, instance, validated_data):
        instance.shop_name = validated_data.get('shop_name', instance.shop_name)
        instance.shop_description = validated_data.get('shop_description', instance.shop_description)
        instance.shop_address = validated_data.get('shop_address', instance.shop_address)
        instance.shop_logo = validated_data.get('shop_logo', instance.shop_logo)
        instance.banner = validated_data.get('banner', instance.banner)
        instance.save()
        return instance
    
