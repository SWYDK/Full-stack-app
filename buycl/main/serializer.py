from rest_framework import serializers
from .models import Clothes
class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['title','anons','full_text','tags','author','pricing','date','isopub','types']