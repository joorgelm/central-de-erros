from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Agent, Event


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password'
        )


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = (
            'id',
            'name',
            'status',
            'env',
            'version',
            'address'
        )


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id',
            'level',
            'data',
            'arquivado',
            'agent',
            'user'
        )
