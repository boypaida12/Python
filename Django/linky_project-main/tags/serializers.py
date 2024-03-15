from rest_framework import serializers
from .models import Tags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Tags