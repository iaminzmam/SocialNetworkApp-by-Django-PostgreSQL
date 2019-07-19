from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegisterForm, StatusForm

from .models import plans
from posts.models import Post



@login_required
def profile(request):
    form = StatusForm(request.POST or None)
    objs = Post.objects.filter(userid=request.user)
    if form.is_valid():
        plan = get_object_or_404(plans, uid=request.user)
        status = form.save(commit=False)
        status.userid = request.user
        status.save()
        plan.status = plan.status - 1
        plan.save()
        return render(request, 'home/index.html', {})

    return render(request, 'accounts/profile.html', {'form': form, 'objs':objs})

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('../plans/')


    context= {'form': form}
    return render(request, 'accounts/login.html', context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        try:
            check_plans = get_object_or_404(plans, uid=request.user.id)
            return redirect('../')
        except:
            return redirect('/plans')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')




@login_required
def plansView(request):

        try:

            check_plans = get_object_or_404(plans, uid=request.user.id)
            return redirect('../../')
        except:
            if request.method == "POST":
                plan_name = request.POST.get('optradio')
                all_plans = {'plan1': [10,25,50], 'plan2': [20,40,70], 'plan3': [30,50,75]}
                status = all_plans[plan_name][0]
                likes = all_plans[plan_name][1]
                comments = all_plans[plan_name][2]
                userid = request.user

                a = plans(uid=userid, likes=likes, comm=comments, status=status)
                a.save()
                return redirect('/')
            return render(request, 'accounts/select-plan.html', {})
