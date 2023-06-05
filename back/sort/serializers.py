from rest_framework import serializers
from .models import Sort


class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        fields = ('array','n')