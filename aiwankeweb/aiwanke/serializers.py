# -*- coding utf-8 -*-
__author__ = 'wei'

from aiwanke.models import GameApp
from apps.rest_framework import serializers

class GameAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameApp
        fields = ('appName','iconUrl','apkUrl','desc','author_name','category_name','create_time','rates')