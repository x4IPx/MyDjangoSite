"""
URL configuration for my_resume project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from django.http import HttpResponse
from my_resume import views
from cv import cv_views
from django.views.generic import TemplateView
from django.views.generic import TemplateView
#Для upload
from django.conf import settings
from django.conf.urls.static import static
from upload.views import image_upload


urlpatterns = [
    path("2", views.index),
    path("", cv_views.index),
    path("contacts/", views.contacts),
    path("feedback", views.feedback),
    path("posttelegram/", views.posttelegram),
    path("base2", views.index2),
    path("contacts2/", views.contacts2),
    path('admin/', admin.site.urls),
    path('advertising', views.hello_def),
    path('t1', views.t1),
    path('index1', views.index1),
    path('index1_2', views.index2),
    path("set", views.set), # Проверка работы кеша , например можно ввести http://IP:8000/set?username=test3
    path("get", views.get), # Получение значения из кеша 
    path("index3", views.index3),
    path("about1/", TemplateView.as_view(template_name="about1.html", extra_context={"yaya_header": "Метод TemplateView говорит что здесь могла быть ваша реклама"})),
    path("upload/", image_upload, name="upload"),
    #path('hello/', hello_def),
]


if bool(settings.DEBUG):

        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
