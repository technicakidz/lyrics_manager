from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from .models import Post

def post_list(request):
    post_list = Post.objects.order_by('-published_date')[:5]
    context = {'post_list': post_list}
    return render(request, 'writers/post_list.html', context)

def detail(request, author_id):
    return HttpResponse("You're looking at author %s." % author_id)
