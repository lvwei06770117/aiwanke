# -*- coding: utf-8 -*-
from aiwanke.models import GameApp
from aiwanke.serializers import GameAppSerializer

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import six
from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger, EmptyPage
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

def index(request):
    game_list = GameApp.objects.order_by('-create_time')
    paginator = Paginator(game_list, 8) # Show 8 contacts per page
    page_number = request.GET.get('page')
    try:
        games = paginator.page(page_number)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)
    except InvalidPage as exc:
        error_format = _('Invalid page (%(page_number)s): %(message)s')
        raise Http404(error_format % {
            'page_number': page_number,
            'message': six.text_type(exc)
        })
    context = {'games': games}
    return render(request, 'aiwanke/index.html', context)

def detail(request,game_id):
    # try:
    #     game = GameApp.objects.get(pk=game_id)
    # except GameApp.DoesNotExist:
    #     raise Http404("游戏不存在")
    game = get_object_or_404(GameApp,pk=game_id)
    return render(request, 'aiwanke/detail.html', {'game': game})

class IndexView(generic.ListView):
    template_name = 'aiwanke/index.html'
    context_object_name = 'game_list'
    paginate_by = '8'

    def get_queryset(self):
        """Return the last five published questions."""
        return GameApp.objects.order_by('-create_time')

class DetailView(generic.DetailView):
    model = GameApp
    template_name = 'aiwanke/detail.html'