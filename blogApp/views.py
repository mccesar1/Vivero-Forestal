from django.shortcuts import render
from blogApp.models import Post
# Create your views here.
def blog(request):
    #importar todos los obetos de la clase blog
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})