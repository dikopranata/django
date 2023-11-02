from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

posts = [{
    'author' : 'John Doe', 'title':'Title 1', 'content':'xaxaxaxaxaaxaxa'
},{
    'author' : 'Mitchell Admin', 'title':'Title 2', 'content':'00d0d0d0d0dd'
}]

def index(request):
    context = {'posts' : posts }
    return render(request, 'polls/index.html', context)
def about(request):
    return render(request, 'polls/about.html')

# def about(request):
#     return HttpResponse("Hello, Django. You're at the ABout.", {'title':'About'})