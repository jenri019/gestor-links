from django.urls import path
from ..views import views_items

urlpatterns = [
    path('all', views_items.get_items),
    path('create', views_items.add_items),
    path('update', views_items.update_items),
    path('delete', views_items.delete_items),
]