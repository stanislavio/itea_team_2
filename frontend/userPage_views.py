from django.shortcuts import render, redirect
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from db.models import User


def user_profile(request, **kwargs):
    context = {}
    user_id = kwargs.get("user_id")
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponse ("That user doesn`t exist.")
    if user:
        context['id'] = user.id
        context['username'] = user.username
        context['email'] = user.email

        is_self = True
        if user.is_authenticated:
            is_self = True

        context['is_self'] = is_self

    return render(request, 'user_profile.html', context)


@login_required
def edit(request, *args, **kwargs):
    user_id = kwargs.get("user_id")
    initial_data = {
        'username': 'Enter your account nickname'
    }
    if request.method =='POST':
        u_form = ProfileEditForm(request.POST, request.FILES, instance=request.user, initial=initial_data)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return HttpResponseRedirect('http://127.0.0.1:8000/user/'+ user_id + '/')
    else:
        u_form = ProfileEditForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'edit.html', context)


def friends_list(request):
    return render(request, 'friends_list.html')
