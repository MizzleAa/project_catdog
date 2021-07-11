from django.db import models

# Create your models here.

class PredictModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='id')
    model_name = models.CharField(max_length=300, verbose_name='model_name')
    model_path = models.CharField(max_length=300, verbose_name='model_path')
    config_path = models.CharField(max_length=300, verbose_name='config_path')
    class Meta:
        db_table = "predict_model"

    def __str__(self):
        return f"{self.id}"

class Record(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='id')
    input_image_path = models.CharField(max_length=300, verbose_name='input_image_path')
    predict_image_path = models.CharField(max_length=300, verbose_name='predict_image_path')
    predict_json_path = models.CharField(max_length=300, verbose_name='predict_json_path')
    register_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='register_time')

    class Meta:
        db_table = "record"

    def __str__(self):
        return f"{self.id}"
