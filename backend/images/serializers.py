from rest_framework import serializers
from .models import Apple

class ApplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apple
        fields = ["id", "color", "photo_url"]
