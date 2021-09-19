from rest_framework_api_key.permissions import BaseHasAPIKey
from .models import UserApiKey
class HasUserAPIKey(BaseHasAPIKey):
    model = UserApiKey