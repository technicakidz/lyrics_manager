from django.http import HttpResponse

from .models import Post

def index(request):
    post_list = Post.objects.order_by('-published_date')[:5]
    context = {'post_list': post_list}
    return render(request, 'writers/index.html', context)

def detail(request, author_id):
    return HttpResponse("You're looking at author %s." % author_id)
