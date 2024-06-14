from rest_framework import serializers
from .models import TTSlot

class TTSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTSlot
        fields = '__all__'
