from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from .models import User
from rest_framework_jwt.utils import jwt_payload_handler
from testpjt import settings
import jwt
from django.contrib.auth.signals import user_logged_in


class UserAPIView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes(IsAuthenticated,)
def get_myinfo(self, request):
    username = ''
    return Response(username, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def login(request):
    username = request.data['username']
    password = request.data['password']
    
    user = User.objects.get(username=username, password=password)
    if user:
        payload = jwt_payload_handler(user)
        token = jwt.encode(payload, settings.SECRET_KEY)
        login_user = {}
        login_user['username'] = user.username
        login_user['token'] = token
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response(login_user, status=status.HTTP_200_OK)
    else:
        res = {'error': 'can not login'}
        return Response(res, status=status.HTTP_403_FORBIDDEN)
    
