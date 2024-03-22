from django.urls import path

from .views import GetItemView, InstertItemView

urlpatterns = [
    path("add", InstertItemView.as_view(), name="insert_view"),
    path("data/", GetItemView.as_view(), name="get_item_view"),
]
