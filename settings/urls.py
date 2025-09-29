from django.contrib import admin
from django.urls import path

from apps.welcome import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("welcome/", views.welcome, name="welcome"),
]
