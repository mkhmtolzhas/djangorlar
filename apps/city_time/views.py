import datetime

from django.shortcuts import render

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def city_time_view(request):
    return render(request, "city_time.html", {"current_time": current_time})
