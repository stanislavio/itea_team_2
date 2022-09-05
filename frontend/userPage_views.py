from django.shortcuts import render, redirect
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def user_profile(request):
    return render(request, 'user_profile.html')


def friends_list(request):
    return render(request, 'friends_list.html')


@login_required
def edit(request):
    initial_data = {
        'username': 'Enter your account nickname'
    }
    if request.method =='POST':
        u_form = ProfileEditForm(request.POST, request.FILES, instance=request.user, initial=initial_data)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user_profile')

    else:
        u_form = ProfileEditForm(instance=request.user)

    context = {
        'u_form': u_form,
        'csrf_token' : csrf.get_token(request),
    }
    return render(request, 'edit.html', context)

    