from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta(serializers.SerializerMetaclass):
        model = User
        fields = ['username', 'password']


class AdvertiserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user = UserSerializer().create(validated_data=validated_data['user'])
        return super(AdvertiserSerializer, self).create({'user': user})

    class Meta(serializers.SerializerMetaclass):
        model = Advertiser
        fields = ['user']


class AdvertiseSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context.get("request")

        if request and hasattr(request, 'user'):
            user = request.user
        else:
            raise serializers.ValidationError({"detail": "no User"})

        validated_data['advertiser'] = user.advertiser
        return super(AdvertiseSerializer, self).create(validated_data)

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
