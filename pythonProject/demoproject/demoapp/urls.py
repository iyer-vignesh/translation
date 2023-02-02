from django.urls import path
from . import views

urlpatterns = [

    path('demo',views.demo,name='demo'),
    path('translate_test',views.translate_test,name='translate_test'),
    # path('download', views.download_file,name='download'),
]