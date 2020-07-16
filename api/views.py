from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action
from .serializers import *
from .models import Agent, Event


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

        user = self.__create_user(request)

        token = Token.objects.create(user=user)

        data = {
            'id': user.id,
            'username': user.username,
            'token': token.key
        }

        return Response(data=data, status=status.HTTP_201_CREATED)

    @staticmethod
    def __create_user(request):

        user = User.objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data['email'],
            is_active=True
        )
        return user


class AgentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    @action(detail=True, methods=['get'])
    def events(self, request, pk):

        events = Event.objects.filter(
            agent_id=pk
        )

        serializer = EventSerializer(events, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventSerializer
