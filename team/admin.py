#!/usr/bir/env python

from django.contrib import admin
from team.models import Player, Basketball

class BasketballAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Basketball, BasketballAdmin)

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(Player, PlayerAdmin)