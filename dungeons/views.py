from django.views.generic import DetailView
from .models import Level
from django.shortcuts import render

# Create your views here.
def dnd_main(request):
    return render(request, 'dungeons/cover.html')

def map(request):
    return render(request, 'dungeons/map.html')

def gauntlet(request):
    return render(request, 'dungeons/gauntlet.html')

def nums(request, id):
    num = int(id)
    return render(request, 'dungeons/nums.html', {'num':num})

class FloorDetailView(DetailView):
    model = Level
    template_name = "dungeons/floor.html"
