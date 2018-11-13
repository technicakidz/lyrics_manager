from django.http import HttpResponse, Http404
from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework import viewsets

from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer

def post_list(request):
    post_lists = Post.objects.order_by('-published_date')[:5]
    context = {'post_lists': post_lists}
    return render(request, 'writers/post_list.html', context)

def detail(request, author_id):
    return HttpResponse("You're looking at author %s." % author_id)
