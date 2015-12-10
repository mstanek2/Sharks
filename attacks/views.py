from django.shortcuts import render

from .models import Shark


def index(request):
    shark_list = Shark.objects.order_by('name')
    context = {'shark_list': shark_list}
    return render(request, 'index.html', context)


def sharkdetail(request, shark_slug):
    shark = Shark.objects.get(name_slug=shark_slug)
    context = {'shark': shark}
    return render(request, 'sharkdetail.html', context)

