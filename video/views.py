from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comment
from django.template.context_processors import csrf


def hello(request):
    video = Video.objects.all()
    comment = Comment.objects.all()
    return render(request, 'index.html', {"video": video, 'comment':comment})
    #return HttpResponse('<h1>hello world</h1>')


def fun(request):
    if request.GET:
        print(request.user.username)
        print(request.GET.get('login'))
        print(request.GET.get('password'))
        print(request.GET.get('comment'))
        return redirect('/hello/')
    if request.POST:
        print(request.user.username)
        print(request.POST.get('label'))
        print(request.POST.get('password'))
        print(request.POST.get('comment'))
        return redirect('/hello/')
    return render(request, "forms.html", csrf(request))
