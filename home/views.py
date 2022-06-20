from django.shortcuts import render
from .models import  *

# Create your views here.

def index(request):
    words_day=Words_of_the_day.objects.all()[:1]
    # slayder=
    context={'words_day':words_day}
    Teach=Teacher.objects.all()
    context={'Teach':Teach}
    return render(request,'index.html' ,context)


def about(request):
    return render(request,'about.html')

def blog(request):
    return render (request, 'blog.html')

