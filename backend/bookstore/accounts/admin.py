from django.contrib import admin
from .models import BaseUserManager, User, Profile, SellerProfile

# Register your models here.

# admin.site.register(BaseUserManager)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(SellerProfile)
