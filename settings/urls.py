from django.contrib import admin
from django.urls import path

from apps.welcome import views
from apps.users import views as user_views
from apps.city_time import views as city_time_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("welcome/", views.welcome, name="welcome"),
    path("users/", user_views.user_list, name="user_list"),
    path("city-time/", city_time_views.city_time_view, name="city_time"),
]
