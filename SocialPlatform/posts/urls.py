from django.urls import path
from django.urls.base import reverse_lazy
from . import views


app_name = 'posts'

urlpatterns = [
    path('create/', views.create_post, name='create'),    
]