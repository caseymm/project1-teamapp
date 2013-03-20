#!/usr/bir/env python

from django.contrib import admin
from team.models import Basketball, Coach

class BasketballAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Basketball, BasketballAdmin)


class CoachAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(Coach, CoachAdmin)