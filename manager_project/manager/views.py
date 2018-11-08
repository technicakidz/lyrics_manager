from django.shortcuts import render
from .models import Post

def post_list(request):
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'manager/post_list.html', {})
