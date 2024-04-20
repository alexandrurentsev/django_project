from django.contrib import admin
from django.urls import path

from project.views import get_home_page, get_about, get_item, get_item_detail

urlpatterns = [
    path("", get_home_page, name="home"),
    path("admin/", admin.site.urls),
    path("about/", get_about, name="about"),
    path("items/", get_item, name="list_items"),
    path("item/<int:item_id>/", get_item_detail, name="item_detail"),
]
