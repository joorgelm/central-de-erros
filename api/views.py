from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.
    The `highlight` field presents a hyperlink to the highlighted HTML
    representation of the code snippet.
    The **owner** of the code snippet may update or delete instances
    of the code snippet.
    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # cadastro usuario
    def create(self, request, *args, **kwargs) -> Response:
        """
        This endpoint presents the users in the system.
        As you can see, the collection of snippet instances owned by a user are
        serialized using a hyperlinked representation.
        """

        user = User.objects.create_user(username=request.data['username'], password=request.data['password'])
        token = Token.objects.create(user=user)
        data = {
            'id': user.id,
            'username': user.username,
            'token': token.key
        }

        return Response(data=data, status=status.HTTP_201_CREATED)
