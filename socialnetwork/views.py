from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from posts.models import Post



#@login_required
def hom(request):
    all_post = Post.objects.all()
    context = { 'posts': all_post }
    return render(request, 'home/index.html', context)


class home(generic.ListView):
    template_name = 'home/home.html'
    def get_queryset(self):
        return Post.objects.all()

