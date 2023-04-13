from django import forms
from django.views.generic import DetailView, UpdateView
from .models import Post

class CreatePost(forms.ModelForm):
    class Meta:
    # name = forms.CharField(label='Name', max_length=200)
    # text = forms.CharField(widget=forms.Textarea(attrs={'rows': '50', 'cols': '150'}))
        model = Post
        fields = ['name', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 120, 'rows': 50}),
        }

