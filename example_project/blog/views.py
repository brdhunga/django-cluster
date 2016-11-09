from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog


def detail_view(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'single.html', {'blog': blog})
