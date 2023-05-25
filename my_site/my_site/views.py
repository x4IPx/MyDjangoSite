# views.py

from django.http import HttpResponse


def hello_def(request):
    print('Кто-то зашёл на главную!')
    return HttpResponse('Здесь могла быть ваша реклама!')


from django.template import loader
def t1(request):
    template = loader.get_template('base.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
