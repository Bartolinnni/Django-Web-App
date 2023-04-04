from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import CreatePost
from django.views.generic import DetailView, UpdateView
from django import forms
# Create your views here.

def index(response):
    return render(response, 'main/home.html')

def register(response):
    return render(response, 'main/register.html')

def blog(response):

    if response.method == 'POST':
        print('witam serdczenie')
        form = CreatePost(response.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            
            t = Post(name=name, text=text)
            t.save()

    else:
        form = CreatePost()

    return render(response, 'main/blog.html', {'form':form})


def searching(response):
    pt = Post.objects.all()
    return render(response, 'main/search.html', {'pt':pt})


class PostDetailView(DetailView):
    model = Post
    template_name = 'main/detail_view.html'


class UpadteYourView(UpdateView):
    model = Post
    template_name = 'main/update_post.html'
    # form_class = CreatePost
    fields = ['name', 'text'.forms.Textarea(attrs={'rows': '50', 'cols': '150'}]