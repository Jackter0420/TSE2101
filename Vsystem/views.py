from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse #just output http output

# Create your views here.

posts = [
    {
        'author':'CoreyMS',
        'title':'System Post 1',
        'content':'First Post Content',
        'date':'Nima',
    },
    {
        'author':'Clement',
        'title':'System Post 2',
        'content':'Second Post Content',
        'date':'Datanoima',
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'Vsystem/home.html', context)

def about(request):
    return render(request,'Vsystem/about.html', {'title':'About'})