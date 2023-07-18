from django.http import HttpResponse
from django.shortcuts import render
from .data import *
import html
from django.utils.html import escape
from forms import TelegramForm
from core import bot

def getSkills():
    i = 0
    gotoshow = ""
    while i < len(yourSkills):
        if skillsPercent[i]:
            skill = "<li><span class='main'>" + yourSkills[i] + "</span><span class='percent'>" + skillsPercent[i]  + "</span></li>"
        else:
            skill = "<li><span class='main full'>" + yourSkills[i] + "</span></li>"
        i += 1
        gotoshow = gotoshow + skill
        if i == len(yourSkills):
            return html.unescape(gotoshow)

def getList(shema):
    i = 0
    gotoshow = ""
    while i < len(shema):
        skill = "<li>" + shema[i] + "</li>"
        i += 1
        gotoshow = gotoshow + skill
        if i == len(shema):
            return html.unescape(gotoshow)

def getListWithYear(shema, year):
    i = 0
    gotoshow = ""
    while i < len(shema):
        if year[i]:
           skill = "<li><span class='main'>" + shema[i] + "</span><span class='year'>" + year[i] + "</span></li>"
        else:
           skill = "<li><span class='main full'>" + shema[i] + "</span></li>"
        i += 1
        gotoshow = gotoshow + skill
        if i == len(shema):
            return html.unescape(gotoshow)

def getListWithLink(shema, link):
    i = 0
    gotoshow = ""
    while i < len(shema):
        if link[i]:
            skill = "<li><a target='_blank' href='" + link[i] + "'>" + shema[i] + "</a></li>"
        else:
            skill = "<li><a target='_blank'>" + shema[i] + "</a></li>"
        i += 1
        gotoshow = gotoshow + skill
        if i == len(shema):
            return html.unescape(gotoshow)

def getSocials(shema, link):
    i = 0
    gotoshow = ""
    while i < len(shema):
        if link[i]:
            skill = "<a class='social' target='_blank' href='" + link[i] + "'><i class='" + shema[i] + "'></i></a>"
            gotoshow = gotoshow + skill
        else:
            gotoshow = gotoshow
        i += 1
        if i == len(shema):
            return html.unescape(gotoshow)

def data():
    userform = TelegramForm()
    return {
        'titleCV' : titleCV,
        'yourName' : yourName,
        'yourProfession' : yourProfession,
        'yourBio' : yourBio,
        'yourCountry' : yourCountry,
        'yourContact' : getSocials(socialContact, yourContact),
        'yourBirthday' : yourBirthday,
        'yourSkills' : getSkills(),
        'yourHobbies' : getList(yourHobbies),
        'yourCerts' : getList(yourCerts),
        'yourEdu' : getListWithYear(yourEdu, eduYear),
        'yourWork' : getListWithYear(yourWork, workYear),
        'yourProject' : getListWithLink(yourProject, projectLink),
        'yourExtras': getList(yourExtras),
        'footerText': footerText ,
        "form": userform
        }

def index(request):
    if request.method == "POST":
        TelegremMessage = request.POST.get("TelegremMessage", "Ошибка которую наврядти ты увидешь")
        bot.post_message(TelegremMessage)
        print(TelegremMessage)
        return HttpResponse(f"<h2>Сообщение отправленно: {TelegremMessage}</h2>")
    else:
        userform = TelegramForm()
#        return render(request, "feedbackDjango.html", {"form": userform})
        return render(request, "cv.html", data())

#def home(request):
    #return render(response, "templates/home.html")


def feedback(request):
    return render(request, "feedback.html")

def feedbackDjango(request):
    if request.method == "POST":
        TelegremMessage = request.POST.get("TelegremMessage", "Ошибка которую наврядти ты увидешь")
        bot.post_message(TelegremMessage)
        print(TelegremMessage)
        return HttpResponse(f"<h2>Сообщение отправленно: {TelegremMessage}</h2>")
    else:
        userform = TelegramForm()
        return render(request, "feedbackDjango.html", {"form": userform})
