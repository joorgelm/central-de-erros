from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, validate_ipv4_address
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User as AuthUser


class Base(models.Model):
    name = models.TextField(max_length=50)

    class Meta:
        abstract = True


class User(AbstractBaseUser):
    last_login = models.DateField(auto_now=True)
    email = models.TextField(max_length=254, validators=[EmailValidator()])
    password = models.TextField(max_length=50, validators=[MinLengthValidator(6)])


class Agent(Base):
    status = models.BooleanField(default=True)
    env = models.TextField(max_length=50)
    version = models.TextField(max_length=5)
    address = models.TextField(max_length=39, validators=[validate_ipv4_address])


class Event(models.Model):

    LEVELS = (
        (0, 'INFO'),
        (1, 'DEBUG'),
        (2, 'WARNING'),
        (3, 'ERROR'),
        (4, 'CRITICAL'),
    )

    def level_validator(level):
        if level not in range(0, 5):
            raise ValidationError('Action not allowed')

    level = models.CharField(max_length=20, choices=LEVELS, validators=[level_validator])
    data = models.TextField(max_length=100, default='')
    detalhes = models.TextField(null=True)
    arquivado = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='agent')
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='user')


class Group(Base):
    pass


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
