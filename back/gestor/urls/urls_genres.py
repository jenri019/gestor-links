from django.urls import path
from ..views import views_genres

urlpatterns = [
    path('all', views_genres.get_genres),
    path('create', views_genres.add_genres),
    path('update', views_genres.update_genres),
    path('delete', views_genres.delete_genres),
]