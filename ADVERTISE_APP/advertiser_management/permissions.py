from rest_framework import permissions
from .models import *


class IsAdvertiser(permissions.BasePermission):

    def has_permission(self, request, view):
        return Advertiser.objects.filter(user=request.user).exists()
