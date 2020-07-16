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

    # def get_level(self, obj):
    #     return obj.get().get_level_display()
    #
    # def get_data(self, obj):
    #     return obj.get().data
