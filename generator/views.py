from django.shortcuts import render
import random
import string


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    length = int(request.GET.get('length', 12))
    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))

    the_password = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'generator/password.html', {'password': the_password})





