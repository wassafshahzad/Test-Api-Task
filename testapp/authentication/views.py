from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .permission import HasUserAPIKey
# Create your views here.
# KEy :  ZtJ60JX1.YHUFSUp4rk0BAco5PvAilMfqFW27kEWc
@api_view(["POST"])
@permission_classes([HasUserAPIKey])
def login_user(request):
    
    if not ("email" in request.POST and "password" in request.POST ):
        return Response({"message" : "Request Params missing"},status=status.HTTP_301_MOVED_PERMANENTLY)
    
    user = authenticate(email=request.data['email'], password=request.data['password'])
    if not user:
        return Response({"message" : "User not found"},status=status.HTTP_401_UNAUTHORIZED)
    else :
        data = {
            'id': user.id,
            "username": user.username,
            "email": user.email,
            "last_login": user.last_login
        }
        return Response(data=data, status=status.HTTP_200_OK)