from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import CreatePost
from django.views.generic import DetailView, UpdateView
from django import forms
from .filters import PostFilter

# from django.contrib.auth.forms import UserCreationForms

# Create your views here.

def index(response):
    return render(response, 'main/home.html')

# def register(response):
#     return render(response, 'main/register.html')

def blog(request):

    if request.method == 'POST':
        print('witam serdczenie')
        form = CreatePost(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']

            t = Post(name=name, text=text)
            t.save()

            request.user.post.add(t)
            # form.save()

            return redirect('/')
        

    else:
        form = CreatePost()

    return render(request, 'main/blog.html', {'form':form})


def searching(request):
    pt = request.user.post.all()

    myFilter = PostFilter(request.GET, queryset=pt)
    pt = myFilter.qs


    return render(request, 'main/search.html', {'pt':pt, 'myFilter':myFilter})


class PostDetailView(DetailView):
    model = Post
    template_name = 'main/detail_view.html'


# class UpadteYourView(UpdateView):
#     model = Post
#     template_name = 'main/update_post.html'
#     form_class = UpdateView

def updatePost(request, pk):

    post = Post.objects.get(id=pk)
    form = CreatePost(instance = post)


    if request.method == 'POST':
        form = CreatePost(request.POST, instance = post)
        
        if form.is_valid():
            # name = form.cleaned_data['name']
            # text = form.cleaned_data['text']

            # t = Post(name=name, text=text)
            # t.save()
            form.save()
            # request.user.post.add(t)
            return redirect('/')


    return render(request, 'main/update_post.html', {'form':form})


def deletePost(request, pk):

    post = Post.objects.get(id = pk)

    if request.method == 'POST':
        post.delete()
        # request.user.post.add(t)
        return redirect('/')


    return render(request, 'main/delete_post.html', {'form':post})



# def register_user(request):
#     return render(request, 'authenticate/register_user.html', {})



