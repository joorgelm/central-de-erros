from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer


class UserViewSetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if view.action == 'create':
                return True
            return False
        return True


class UserViewSet(viewsets.ModelViewSet):

    permission_classes = [UserViewSetPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # cadastro usuario
    def create(self, request, *args, **kwargs) -> Response:

        user = User.objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data['email'],
            is_active=True
        )
        token = Token.objects.create(user=user)
        data = {
            'id': user.id,
            'username': user.username,
            'token': token.key
        }

        return Response(data=data, status=status.HTTP_201_CREATED)
