# -*- coding utf-8 -*-

from aiwanke.models import GameApp
from aiwanke.serializers import GameAppSerializer

from django.http import HttpResponse
from apps.rest_framework import generics
from apps.rest_framework import mixins

class GameAppListView(mixins.ListModelMixin,
                  generics.GenericAPIView):
    #queryset = GameApp.objects.all()
    serializer_class = GameAppSerializer

    def get_queryset(self):
        try:
            game_source = int(self.kwargs['source'])
        except (KeyError,TypeError, ValueError):
            game_source = 0

        if game_source > 0:
            applist = GameApp.objects.filter(source=game_source)
        else:
            applist = GameApp.objects.all()

        return applist

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

def home(request):
    return HttpResponse("Hello, world. You're at the aiwanke index.")

