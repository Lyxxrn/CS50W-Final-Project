from pydoc import describe
from typing import List
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import Http404

from datetime import datetime
from .models import News, Event

# Create your views here.

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("member"))
        else:
            return render(request, "login.html", {
                "message": "Ungültiges Passwort oder Name."
            })
    else:
        
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def index(request):
    return render(request, "index.html")

@login_required(login_url='/login') 
def member(request):
    return render(request, "member.html")

@login_required(login_url='/login')
def news(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        time = datetime.today().strftime('%Y-%m-%d')
        News.objects.create(title=title, content=content, time=time)
        return render(request, "member.html", {
            'message': "Der Eintrag wurde erfolgreich veröffentlicht."
        })

    else:
        return render(request, "index.html")

@login_required(login_url='/login')
def event(request):
    if request.method == "POST":
        title = request.POST.get('title')
        date = request.POST.get('date')
        describtion = request.POST.get('describtion')
        Event.objects.create(title=title, date=date, describtion=describtion)
        return render(request, "member.html", {
            'message': "Das Event wurde erfolgreich veröffentlicht."
        })

    else:
        return render(request, "index.html")

def news_view(request, title):
    try:
        news = News.objects.get(title=title)
        return render(request, "news.html", {
                    'news': news
                })
    except:
        return HttpResponseNotFound('Diese Seite existiert leider nicht.')

@login_required
def news_edit(request, title):
    if request.method == "GET":
        news = News.objects.get(title=title)
        return render(request, "news-edit.html", {
                    'news': news
                })
    else:
        newtitle = request.POST.get('title')
        content = request.POST.get('content')

        news = News.objects.get(title=title)
        news.title = newtitle
        news.content = content
        news.save()
        return render(request, "member.html", {
            'message': "Die Seite wurde erfolgreich bearbeitet."
        })

@login_required
def event_edit(request, title):
    if request.method == "GET":
        event = Event.objects.get(title=title)
        return render(request, "eventedit.html", {
                    'event': event
                })
    else:
        newtitle = request.POST.get('title')
        date = request.POST.get('date')
        describtion = request.POST.get('describtion')

        event = Event.objects.get(title=title)
        event.title = newtitle
        event.date = date
        event.describtion = describtion
        event.save()
        return render(request, "member.html", {
            'message': "Das Event wurde erfolgreich bearbeitet."
        })

# small API based on the mail project API

@login_required
def get_news(request):
    news = News.objects.all()
    return JsonResponse([i.serialize() for i in news], safe=False)

@login_required
def get_events(request):
    events = Event.objects.all()
    return JsonResponse([i.serialize() for i in events], safe=False)
