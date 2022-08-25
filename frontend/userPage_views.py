from django.shortcuts import render, redirect
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def user_profile(request):
    return render(request, 'user_profile.html')


@login_required
def edit(request):
    if request.method =='POST':
        u_form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user_profile')

    else:
        u_form = ProfileEditForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'edit.html', context)

    