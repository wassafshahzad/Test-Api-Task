from django.contrib import admin
from .models import CustomUser, UserApiKey
from rest_framework_api_key.admin import APIKeyModelAdmin
# Register your models here.



class UserApiKeyAdmin(APIKeyModelAdmin):
    pass


admin.site.register(CustomUser)
admin.site.register(UserApiKey, UserApiKeyAdmin)