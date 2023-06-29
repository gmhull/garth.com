from django.shortcuts import render

def error_404(request, exception):
    return render(request, 'projects/404.html')

def error_500(request):
    return render(request, 'projects/500.html')
