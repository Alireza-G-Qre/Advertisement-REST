from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta(serializers.SerializerMetaclass):
        model = User
        fields = ['username', 'email']


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta(serializers.SerializerMetaclass):
        model = Advertiser
        fields = ['user', 'active']


class AdvertiseSerializer(serializers.ModelSerializer):
    class Meta(serializers.SerializerMetaclass):
        model = Ad
        fields = ['title', 'linkUrl', 'img_Url', 'description']


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
