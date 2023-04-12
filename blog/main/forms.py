from django import forms

class CreatePost(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': '50', 'cols': '150'}))
