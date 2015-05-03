# -*- coding: utf-8 -*-
from django.contrib import admin

from aiwanke.models import GameApp

class GameAppAdmin(admin.ModelAdmin):
    #fields = ['appName','iconUrl','apkUrl','create_time','editor','source']
    list_display = ('appName','iconUrl','apkUrl','create_time','editor','source')
    list_filter = ['source']
    search_fields = ['appName']
    fieldsets = [
        ('基本信息',{'fields':['appName','iconUrl','apkUrl','source','editor']}),
        ('互动信息',{'fields':['download_cnt','view_cnt','rates']}),
    ]
admin.site.register(GameApp,GameAppAdmin)