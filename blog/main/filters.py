import django_filters
from django_filters import CharFilter


from .models import Post

class PostFilter(django_filters.FilterSet):

    text = CharFilter(field_name='text', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Post
        fields = ['name', 'text']
