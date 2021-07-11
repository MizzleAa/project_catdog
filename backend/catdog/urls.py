from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static

from .views import RecordCreate, RecordDelete, RecordList, RecordUpdate, RecordRetrieve

app_name = 'catdog'

urlpatterns = [
    path('list/',
         RecordList.as_view(), name='record_list'),
    path('create/',
         RecordCreate.as_view(), name='record_create'),
    path('retrieve/<int:pk>',
         RecordRetrieve.as_view(), name='record_retrieve'),
    path('update/<int:pk>',
         RecordUpdate.as_view(), name='record_update'),
    path('delete/<int:pk>',
         RecordDelete.as_view(), name='record_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

