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



def index1(request):
    template = loader.get_template('index1.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


from django.http import HttpResponse
 
def index2(request):
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    path = request.path     # получаем запрошенный путь
    return HttpResponse(f"""
             <p>Host: {host}</p>
             <p>Path: {path}</p>
             <p>User-agent: {user_agent}</p>
             """)
