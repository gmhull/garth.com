from django.views.generic import DetailView
from .models import Level
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def dnd_main(request):
    return render(request, 'dungeons/cover.html')

def map(request):
    return render(request, 'dungeons/map.html')

def gauntlet(request):
    return render(request, 'dungeons/gauntlet.html')

def no_access(request):
    return render(request, 'dungeons/no_access.html')

@login_required
def end(request):
    return render(request, 'dungeons/gauntlet_end.html')

@login_required
def show_level(request, level):
    MAX_LEVEL = 10
    current_user = request.user.profile
    current_level = current_user.dungeon_depth
    if current_level == MAX_LEVEL and current_user.completed:
        return HttpResponseRedirect('end')

    level_obj = get_object_or_404(Level, floor_number=int(level))

    if request.method == 'GET':
        if current_level >= int(level) and int(level) > 0:
            return render(request, 'dungeons/level.html', {'level': level_obj})
        # elif current_level > int(level) and int(level) > 0:
        #     return HttpResponseRedirect(f'level_{int(level)}')
        else:
            return HttpResponseRedirect(f'level_{current_level}')

    elif request.method == 'POST':
        user_answer = request.POST['answer']
        print(user_answer)
        if level_obj.password_check(user_answer):
            if current_user.delve_down():
                return HttpResponseRedirect('end')
            return HttpResponseRedirect(f'level_{int(level)+1}')
        return HttpResponseRedirect(f'level_{int(level)}')

class FloorDetailView(DetailView):
    model = Level
    template_name = "dungeons/floor.html"
