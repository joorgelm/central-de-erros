from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, validate_ipv4_address
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser


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

    ACTIONS = (
        (0, 'INFO'),
        (1, 'DEBUG'),
        (2, 'WARNING'),
        (3, 'ERROR'),
        (4, 'CRITICAL'),
    )

    def action_validator(self, action):
        if action not in self.ACTIONS:
            raise ValidationError('Action not allowed')

    level = models.TextField(max_length=20, choices=ACTIONS, validators=[action_validator])
    data = models.TextField(max_length=20)
    arquivado = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(Base):
    pass


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
