#!/usr/bir/env python

from django.contrib import admin
from team.models import Football, Basketball, Baseball, Coach

class BasketballAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Basketball, BasketballAdmin)

class FootballAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(Football, FootballAdmin)

class BaseballAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(Baseball, BaseballAdmin)

class CoachAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(Coach, CoachAdmin)