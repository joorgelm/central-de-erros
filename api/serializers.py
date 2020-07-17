from abc import ABC

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


class EventSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(EventSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    # agent = serializers.SerializerMethodField()
    # user = UserSerializer(many=True)
    # level = serializers.SerializerMethodField()
    # data = serializers.SerializerMethodField()

    class Meta:
        ordering = ['-id']
        model = Event
        fields = (
            'id',
            'level',
            'data',
            'arquivado',
            'agent',
            'user'
        )
        read_only_fields = ['id']


class EventFrequencySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    level = serializers.IntegerField()
    data = serializers.CharField()
    arquivado = serializers.BooleanField()
    date = serializers.DateField()
    user_id = serializers.IntegerField()
    frequency = serializers.IntegerField()
