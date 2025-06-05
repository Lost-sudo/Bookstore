from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer, RegisterSerializer, SellerProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        if hasattr(request.user, 'profile'):
            return Response({'detail': 'Profile already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SellerProfileView(APIView):
    serializer_class = SellerProfileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        if hasattr(request.user, 'seller_profile'):
            return Response({'detail': 'Seller profile already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SellerProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            seller_profile =request.user.seller_profile
        except SellerProfile.DoesNotExist:
            return Response({'detail': 'Seller profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SellerProfileSerializer(seller_profile, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            seller_profile = request.user.seller_profile
        except SellerProfile.DoesNotExist:
            return Response({'detail': 'Seller profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SellerProfileSerializer(seller_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
