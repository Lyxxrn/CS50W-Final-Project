
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("member", views.member, name='member'),
    path("news", views.news, name="news"),
    path("event", views.event, name="event"),
    path("news/edit", views.news_edit, name="news_edit"),
    path("event/edit", views.event_edit, name="event_edit"),
    path("news_edit/<str:title>", views.news_edit, name="news_edit"),
    path("event_edit/<str:title>", views.event_edit, name="event_edit"),

    # API Routes
    path("news_view/<str:title>", views.news_view, name="news_view"),
    path("get_news", views.get_news, name="get_news"),
    path("get_events", views.get_events, name="get_events"),
]
