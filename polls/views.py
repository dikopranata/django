from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import HttpResponse

posts = [{
    'author' : 'John Doe', 'title':'Title 1', 'content':'xaxaxaxaxaaxaxa'
},{
    'author' : 'Mitchell Admin', 'title':'Title 2', 'content':'00d0d0d0d0dd'
}]

rooms = [{
    'id' : 1, 'name' : 'Diko'
}, {
    'id' : 2, 'name' : 'Pranata'
},{
    'id' : 3, 'name' : 'John'
}]

def index(request):
    context = {'posts' : posts, 'title': 'Judul', 'rooms':rooms }
    #context = { 'posts' : Post.objects.all }
    return render(request, 'polls/index.html', context)
def about(request):
    context = { 'posts' : Post.objects.all }
    return render(request, 'polls/about.html', context)
def home(request):
    context = {'rooms': rooms }
    return render(request,'polls/home.html',context)
def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room' : room}
    return render(request,'polls/room.html',context)
# def about(request):
#     return HttpResponse("Hello, Django. You're at the ABout.", {'title':'About'})