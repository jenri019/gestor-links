from django.urls import path
from ..views import views_items

urlpatterns = [
    path('all', views_items.get_items),
]