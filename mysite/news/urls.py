from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('news/', news, name = 'news'),
    path('create/', create, name = 'create'),
]