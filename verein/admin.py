from django.contrib import admin
from .models import User, News, Event
# Register your models here.
admin.site.register(User)
admin.site.register(News)
admin.site.register(Event)