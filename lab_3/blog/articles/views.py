from django.shortcuts import render
from django import template
from .models import Article


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

