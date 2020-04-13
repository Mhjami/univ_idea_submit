from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User

from django.views import generic
from .models import Post

from .forms import CreatePost


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def getCreatePostPage(response):
    if response.method == "POST":
        form = CreatePost(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CreatePost()
        return render(response,"post idea.html", {"form":form})

