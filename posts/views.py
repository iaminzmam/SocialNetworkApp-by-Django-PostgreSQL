from django.shortcuts import render
from django.views import  generic
from django.shortcuts import get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from posts.models import Post
from accounts.models import plans

# Create your views here.

class PostView(generic.DetailView):
    model = Post
    template_name = 'posts/details.html'

@login_required
def LikePost(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    plan = get_object_or_404(plans, uid=request.user)
    if request.user.id in post.likes:
        post.likes.remove(request.user.id)
        plan.likes = plan.likes + 1
        post.save()
        plan.save()
    else:
        post.likes.append(request.user.id)
        plan.likes = plan.likes - 1
        post.save()
        plan.save()
    return redirect('/post/' + request.POST.get('post_id'))


@login_required
def addComment(request):
    post  = get_object_or_404(Post,id=request.POST.get('post_id'))
    plan = get_object_or_404(plans, uid=request.user)
    if request.user.id:
        uid = request.user.id
        uname = request.user.username
        created = timezone.now()
        data = request.POST.get('com_box')
        post.comments.append([data,created,uid,uname])
        post.save()
        plan.comm = plan.comm - 1
        plan.save()
        return redirect('/post/'+str(request.POST.get('post_id')))




@login_required
def delComment(request):
    post = get_object_or_404(Post, id=equest.POST.get('cmnt'))
    plan = get_object_or_404(plans, uid=request.user)
    if request.user.is_authenticated:
        seq = request.POST.get('obj')
        ok = post.comments.pop(int(seq))
        post.save()
        if ok:
            plan.comm = plan.comm + 1
            plan.save()
        return redirect('/post/' + request.POST.get('cmnt'))
    return redirect('/post/' + request.POST.get('cmnt'))