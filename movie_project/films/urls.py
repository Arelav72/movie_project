from django.urls import path
from .views import create_film, film_list

urlpatterns = [
    path('create/', create_film, name='create_film'),
    path('list/', film_list, name='film_list'),
]