# views.py

from django.http import HttpResponse
from my_resume import bot
from forms import TelegramForm


def index(request):
    return render(request, "index.html")

def contacts(request):
    return render(request, "contacts.html")

def feedback(request):
    return render(request, "feedback.html")

def feedbackDjango(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    else:
        userform = TelegramForm()
        return render(request, "feedbackDjango.html", {"form": userform})



def posttelegram(request):
    # получаем из данных запроса POST отправленные через форму данные
    telegram_text = request.POST.get("text", "Undefined")
    #name = request.POST.get("name", "Undefined")
    #age = request.POST.get("age", 1)
    bot.post_message(telegram_text)
    print(telegram_text)
    return HttpResponse(f"<h2>Спасибо за отзыв! Отпавленное сообщение : {telegram_text} </h2>")


def hello_def(request):
    print('Кто-то зашёл на главную!')
    return HttpResponse('Здесь могла быть ваша реклама!')


from django.template import loader
def t1(request):
    template = loader.get_template('base4.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)



def index1(request):
    template = loader.get_template('index1.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


from django.http import HttpResponse
 
def index1_2(request):
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




from django.shortcuts import render

def index2(request):
    return render(request, "index2.html")

def contacts2(request):
    return render(request, "contacts2.html")


