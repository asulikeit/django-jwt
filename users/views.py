from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from .models import User
from rest_framework_jwt.utils import jwt_payload_handler
from testpjt import settings
import jwt
from django.contrib.auth import authenticate, logout, login


class UserAPIView(APIView):
    permission_classes = (IsAdminUser,)
    mapper = UserSerializer
    entity = User.objects
    
    def post(self, request):
        user = request.data
        serializer = self.mapper(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        users = self.entity.all()
        serializer = self.mapper(users, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_myinfo(self):
    username = self.user.username
    return Response(username, status=status.HTTP_200_OK)


def _generate_jwt_token(user):
    payload = jwt_payload_handler(user)
    token = jwt.encode(payload, settings.SECRET_KEY)
    login_user = {}
    login_user['username'] = user.username
    login_user['token'] = token
    return login_user


@api_view(['POST'])
@permission_classes([AllowAny, ])
def login_by_basic(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user:
        login_user = _generate_jwt_token(user)
        login(request, user)
        return Response(login_user, status=status.HTTP_200_OK)
    else:
        res = {'error': 'can not login'}
        return Response(res, status=status.HTTP_403_FORBIDDEN)

    
@api_view(['GET'])
def logout_by_token(request):
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)
