from django.shortcuts import render,redirect
from .models import Post,Topic
# Create your views here.
from django.http import HttpResponse
from .forms import PostForm

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
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    #posts = Post.objects.all()
    posts = Post.objects.filter(topic__name__icontains=q)
    topics = Topic.objects.all()

    context = {'rooms': rooms, 'posts' : posts, 'topics':topics }
    return render(request,'polls/home.html',context)
def room(request, pk):
    room = None
    for i in rooms:
       if i['id'] == int(pk):
           room = i
    #room = Post.objects.get(id=pk)
    context = {'room' : room}
    return render(request,'polls/room.html',context)
def post(request,pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request,'polls/post.html',context)
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form' : form}
    return render(request,'polls/post_form.html',context)

def updatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'polls/post_form.html',context)

def deletePost(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request,'polls/delete.html',{'obj':post})


# def about(request):
#     return HttpResponse("Hello, Django. You're at the ABout.", {'title':'About'})