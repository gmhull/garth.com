from django.views.generic import DetailView
from dungeons.models import Level
from facial_recognition.models import Screenshot
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlopen
from datetime import datetime

# Create your views here.
def dnd_main(request):
    return render(request, 'dungeons/cover.html')

def map(request):
    return render(request, 'dungeons/map.html')

def gauntlet(request):
    if request.method == "POST":
        image_path = request.POST["img_src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
        image = NamedTemporaryFile()
        image.write(urlopen(image_path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name = str(image.name).split('/')[-1]
        name += '.jpg'  # store image in jpeg format
        image.name = name
        if image is not None:
            img_datetime = datetime.now()
            img_datetime = img_datetime.strftime("%d/%m/%Y %H:%M:%S")
            obj = Screenshot(username=img_datetime, image=image)  # create a object of Image type defined in your model
            obj.save()
            request.session["img_id"] = obj.username  #url to image stored in my server/local device
        else:
            return redirect('/')
        return redirect('recognize')
    return render(request, 'dungeons/gauntlet.html')

def no_access(request):
    return render(request, 'dungeons/no_access.html')

@login_required
def end(request):
    return render(request, 'dungeons/gauntlet_end.html')

@login_required
def enterance(request):
    return render(request, 'dungeons/enterance.html')

@login_required
def show_level(request, level):
    MAX_LEVEL = 10
    current_user = request.user.profile
    current_level = current_user.dungeon_depth
    if current_level == MAX_LEVEL and current_user.completed:
        return redirect('end')

    level_obj = get_object_or_404(Level, floor_number=int(level))

    if request.method == 'GET':
        if current_level >= int(level) and int(level) > 0:
            return render(request, 'dungeons/level.html', {'level': level_obj})
        else:
            return redirect('level', int=current_level)

    elif request.method == 'POST':
        user_answer = request.POST['answer']
        if level_obj.password_check(user_answer):
            if current_user.delve_down():
                return redirect('gauntlet_end')
            return redirect('level', int=level+1)
        return redirect('level', int=level)
class FloorDetailView(DetailView):
    model = Level
    template_name = "dungeons/floor.html"
