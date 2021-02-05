from rest_framework import serializers
from .models import *


class OwnerSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    rePassword = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super(OwnerSerializer, self).__init__(*args, **kwargs)
        if kwargs['rePassword']:
            self.fields.append('rePassword')

    def validate(self, data):
        if data['password'] != data['rePassword'] and 'rePassword' in data:
            raise serializers.ValidationError("Passwords not the same  :(")

    class Meta(serializers.SerializerMetaclass):
        fields = ['username', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta(serializers.SerializerMetaclass):
        model = User
        fields = ['username', 'email', 'password']


class AdvertiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta(serializers.SerializerMetaclass):
        model = Advertiser
        fields = ['owner', 'active']


class AdvertiseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='advertiser.user.username')

    class Meta(serializers.SerializerMetaclass):
        model = Ad
        fields = ['owner', 'title', 'linkUrl', 'img_Url', 'description']


class ViewAdSerializer(serializers.ModelSerializer):
    class Meta(serializers.SerializerMetaclass):
        model = ViewAd
        fields = ['ad_user_id', 'ip', 'time']
        depth = 2


class ClickAdSerializer(serializers.ModelSerializer):
    class Meta(serializers.SerializerMetaclass):
        model = ViewAd
        fields = ['ad_user_id', 'ip', 'time']
        depth = 2
