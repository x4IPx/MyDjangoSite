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


from django.http import HttpResponse

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response


# получение куки
def get(request):
    # получаем куки с ключом username
    try:
        # получаем куки с ключом username
        username = request.COOKIES["username"]
        return HttpResponse(f"Hello {username}")
    except:
        print('ttt')
        return HttpResponse('В куках ничего нет')


from django.shortcuts import render

def index3(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "index3.html", context=data)
