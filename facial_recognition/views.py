from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .backend import FaceRecognition
from .models import Screenshot
# Create your views here.
def face_recog(request):
    return render(request, 'facial_recognition/index.html')

def recognize(request):
    img_id = request.session["img_id"]
    img_obj = Screenshot.objects.get(username=img_id)
    img_url = img_obj.image.url
    face_detection = FaceRecognition(img_url)
    face_match, password = face_detection.compare_faces()
    user = authenticate(request, username=face_match, password=password)
    img_obj.delete()
    if user is not None:
        login(request, user)
        return redirect('enterance')
    else:
        return redirect('no_access')
