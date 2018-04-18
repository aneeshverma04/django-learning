from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

# Using generic views ==> ListView , DetailView
urlpatterns = [
    url('^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
        template_name='blog/blog.html')),
    # - as descending so see latest posts.. [:25] is limit by
    url('^(?P<pk>\d+)$', DetailView.as_view(model = Post,template_name = 'blog/post.html')),

    # (?P)above is Named groups...pk is primary key(here is id)...\d = digit.. + ==> 1 or more...
    # primary key which happens to be a digit
]
