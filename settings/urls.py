from django.contrib import admin
from django.urls import path

from apps.welcome import views
from apps.users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("welcome/", views.welcome, name="welcome"),
    path("users/", user_views.user_list, name="user_list"),
]
