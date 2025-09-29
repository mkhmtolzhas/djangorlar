from django.shortcuts import render

users = [
    {'first_name': 'John', 'last_name': 'Doe'},
    {'first_name': 'Jane', 'last_name': 'Smith'},
    {'first_name': 'Alice', 'last_name': 'Johnson'},
]


def user_list(request):
    return render(request, 'users.html', {'users': users})
