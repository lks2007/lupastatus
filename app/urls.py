from django.urls import path
from django.conf import settings

from . import views

app_name='chatlive'

urlpatterns = [
    path('', views.index, name="index")
    # path('favicon.ico', )
]