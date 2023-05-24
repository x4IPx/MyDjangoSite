# views.py

from django.http import HttpResponse


def hello_def(request):
    print('Кто-то зашёл на главную!')
    return HttpResponse('Здесь могла быть ваша реклама!')
