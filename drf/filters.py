from blogapp.models import Blog
from django_filters import FilterSet


class BlogFilter(FilterSet):
    class Meta:
        model = Blog
        fields = ["category", ]