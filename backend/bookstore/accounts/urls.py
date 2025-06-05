from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterView, ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('profile/', ProfileView.as_view(), name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
