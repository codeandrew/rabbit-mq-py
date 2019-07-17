from rest_framework import serializers
from .models import Items


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'subtitle', 'type', 'iconUrl', 'mallId', 'keyword')
        depth = 1
