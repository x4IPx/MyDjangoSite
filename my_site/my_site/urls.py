"""
URL configuration for my_site project.

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
from my_site import views
from django.views.generic import TemplateView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello_def),
    path('t1', views.t1),
    path('index1', views.index1),
    path('index2', views.index2),
    path("set", views.set),
    path("get", views.get),
    path("index3", views.index3),
    path("about1/", TemplateView.as_view(template_name="about1.html", extra_context={"yaya_header": "Метод TemplateView говорит что здесь могла быть ваша реклама"})),
    #path('hello/', hello_def),
]
