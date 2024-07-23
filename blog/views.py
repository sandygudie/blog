from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog
from django.template import loader


def index(request):
    data = Blog.objects.filter(published=True, featured_post=False).values()
    featured = Blog.objects.filter(published=True, featured_post=True).values()
    context = {"bloglists": data, "featuredpost": featured}
    return render(request, "blog/index.html", context)


def about(request):
    return render(request, "blog/about.html")


def blog(request, slug):
    recent_post = Blog.objects.filter(published=True, featured_post=False)[:5]
    data = Blog.objects.get(slug=slug)
    context = {"post": data, "recent_post": recent_post}
    return render(request, "blog/blog_details.html", context)
