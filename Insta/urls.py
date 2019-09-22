from django.urls import path
from . import views

urlpatterns = [
    path('', views.HellowWorld.as_view(), name = 'helloword')
]