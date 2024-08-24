from rest_framework import serializers
from .models import Image, APIMetrics, FunctionMetrics, AggregateMetrics

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class APIMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIMetrics
        fields = '__all__'
