from django.shortcuts import render
from .models import Feed

def index(request):
    feeds = Feed.objects.order_by('-pk')
    context = {
        'feeds' : feeds,
    }
    return render(request, 'feeds/index.html', context)