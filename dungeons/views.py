from django.shortcuts import render

# Create your views here.
def dnd_main(request):
    return render(request, 'dungeons/index.html')
