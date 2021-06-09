from django.shortcuts import render


def index(request):
    return render(request, 'personal/cover_page.html')

def contact(request):
    return render(request, 'personal/contact.html', {'content': ['If you would like to contact me, please email me','gmhull@wpi.edu']})

def about(request):
    return render(request, 'personal/about.html')

def trythis(request):
    return render(request, 'dungeons/index.html')
