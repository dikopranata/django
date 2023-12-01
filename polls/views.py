from django.shortcuts import render,redirect
from .models import Post,Topic,Comment
from django.db.models import Q
from django.contrib.auth.decorators import login_required
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

@login_required
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    #posts = Post.objects.all()
    posts = Post.objects.filter(
        Q(topic__name__icontains=q) |
        Q(title__icontains=q)|
        Q(content__icontains=q)
        )
    post_count = posts.count()
    topics = Topic.objects.all()
    comments = Comment.objects.all()
    context = {'rooms': rooms, 'posts' : posts, 'topics':topics,'post_count':post_count,'comments':comments }
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
    comments = post.comment_set.all().order_by('-created')

    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            post = post,
            body = request.POST.get('body')
        )
        return redirect('post',pk=post.id)
    context = {'post':post,'comments':comments}
    return render(request,'polls/post.html',context)

@login_required
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form' : form}
    return render(request,'polls/post_form.html',context)

@login_required
def updatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.user != post.author:
        return HttpResponse('You are not allowed here!')
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'polls/post_form.html',context)

@login_required
def deletePost(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request,'polls/delete.html',{'obj':post})


# def about(request):
#     return HttpResponse("Hello, Django. You're at the ABout.", {'title':'About'})