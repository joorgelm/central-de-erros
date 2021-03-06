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
        read_only_fields = ['id']


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
        read_only_fields = ['id']


class EventSerializerDetail(serializers.ModelSerializer):

    agent = AgentSerializer()
    user = UserSerializer()

    class Meta:
        model = Event
        fields = (
            'id',
            'level',
            'data',
            'detalhes',
            'date',
            'arquivado',
            'agent',
            'user'
        )
        read_only_fields = ['id']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id',
            'level',
            'data',
            'detalhes',
            'date',
            'arquivado',
            'agent',
            'user'
        )
        read_only_fields = ['id']


class EventFrequencySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    level = serializers.IntegerField()
    data = serializers.CharField()
    detalhes = serializers.CharField()
    arquivado = serializers.BooleanField()
    date = serializers.DateField()
    user_id = serializers.IntegerField()
    frequency = serializers.IntegerField()
