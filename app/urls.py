from django.urls import path
from .views import st_registre

urlpatterns = [
    path('', st_registre, name='st_registre'),
]