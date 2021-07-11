from rest_framework import serializers
from .models import PredictModel, Record

class PredictModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 
            'model_name', 
            'model_path',
            'config_path',
        )
        model = PredictModel


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'input_image_path',
            'predict_image_path',
            'predict_json_path',
        )
        model = Record

