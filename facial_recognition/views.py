from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .backend import FaceRecognition, FaceTest
# Create your views here.
def face_recog(request):
    return render(request, 'facial_recognition/index.html')

def recognize(request):
    face_detection = FaceRecognition()
    face_match, password = face_detection.compare_faces()
    print(face_match, password)
    user = authenticate(request, username=face_match, password=password)
    if user is not None:
        login(request, user)
        return redirect('/dungeons/enterance')
    else:
        return redirect('/dungeons/no_access')

def recog(request):
    face_detection = FaceTest()
    face_match, password = face_detection.run()
    user = authenticate(request, username=face_match, password=password)
    if user is not None:
        login(request, user)
        return redirect('/dungeons/enterance')
    else:
        return redirect('/dungeons/no_access')
