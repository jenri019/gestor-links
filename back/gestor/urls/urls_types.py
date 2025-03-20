from django.urls import path
from ..views import views_types

urlpatterns = [
    path('all', views_types.get_types),
    path('create', views_types.add_types),
]