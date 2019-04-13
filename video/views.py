from django.shortcuts import render
from django.http import HttpResponse
from .models import Video, Comment


def hello(request):
    video = Video.objects.all()
    comment = Comment.objects.all()
    return render(request, 'index.html', {"video": video, 'comment':comment})
    #return HttpResponse('<h1>hello world</h1>')
# Create your views here.
