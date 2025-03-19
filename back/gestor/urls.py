from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('all', views.get_genres),
    path('create', views.add_genres),
    path('update', views.update_genres),
]