from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import RecordSerializer, PredictModelSerializer
from .models import Record, PredictModel

from .ai.predict import predict

import os
import datetime
from PIL import Image
class RecordList(APIView):
    def post(self, request, format=None):
        record = Record.objects.all()
        serializer = RecordSerializer(record, many=True)
        return Response(serializer.data)


class RecordCreate(APIView):
    def post(self, request, format=None):

        now = datetime.datetime.now()
        str_datetime = now.strftime('%Y%m%d_%H%M%S')

        input_file_name = f"input_{str_datetime}_{request.data['input_file_name']}"
        predict_file_name = f"predict_{str_datetime}_{request.data['input_file_name']}"

        files = request.data["files"]

        path = default_storage.save(input_file_name, ContentFile(files.read()))
        
        predict_options = {
            #"model_root":"faster_rcnn",
            #"model_name": "faster_rcnn_r50_fpn_1x_coco",
            "model_root":"cascade_rcnn",
            "model_name": "cascade_mask_rcnn_x101_32x4d_fpn_1x_coco",
            "input_file_name":input_file_name,
            "predict_file_name":predict_file_name
        }
        input_image_path, predict_image_path, predict_json_path, predict_jsons = predict.run(predict_options)

        fields ={}
        fields["input_image_path"] = input_image_path
        fields["predict_image_path"] = predict_image_path
        fields["predict_json_path"] = predict_json_path
        
        serializer = RecordSerializer(data=fields)

        if serializer.is_valid():
            serializer.save()
            urls = f"http://127.0.0.1:8000/catdog{settings.MEDIA_URL}" 
            output = {}
            output["input_image_url"] = urls + input_image_path.split("\\")[-1]
            output["predict_image_url"] = urls + predict_image_path.split("\\")[-1]
            output["predict_result"] = predict_jsons

            return Response(output, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecordRetrieve(APIView):
    def post(self, request, pk, format=None):
        sampleTable = Record.objects.get(pk=pk)
        serializer = RecordSerializer(sampleTable)
        return Response(serializer.data)


class RecordDelete(APIView):
    def post(self, request, pk, format=None):
        sampleTable = Record.objects.get(pk=pk)
        sampleTable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecordUpdate(APIView):
    def post(self, request, pk, format=None):
        sampleTable = Record.objects.get(pk=pk)
        serializer = RecordSerializer(sampleTable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
