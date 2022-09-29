from django.shortcuts import render, redirect
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from db.models import User, FriendRequest
from django.middleware import csrf


def user_profile(request, user_id=None, *args, **kwargs):
    if request.user.is_authenticated:
        if request.user.id == user_id or user_id is None:
            self_page = True
            user = request.user
            context = {
                'user': user,
                'self_page': self_page,
                'username': user.username,
                'email': user.email,
                'photo': user.photo,
                'phone': user.phone,
                'short_bio': user.short_bio,
                'hide_email': user.hide_email,
                'hide_phone': user.hide_phone,
                'get_friends_number': user.get_friends_number,
                'get_friends': user.get_friends
            }
            return render(request, 'user_profile.html', context)
        if request.user.id != user_id:
            user = request.user.id
            account = User.objects.get(pk=user_id)
            context = {
                'account': account,
                'username': account.username,
                'email': account.email,
                'photo': account.photo,
                'phone': account.phone,
                'short_bio': account.short_bio,
                'hide_email': account.hide_email,
                'get_friends_number': account.get_friends_number
            }
            return render(request, 'user_profile.html', context)
    else:
        return HttpResponse('<h1> Please, Sign_in </h1>')


@login_required
def edit(request, *args, **kwargs):
    if request.method =='POST':
        u_form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user_profile')
    else:
        u_form = ProfileEditForm(instance=request.user)

    context = {
        'u_form': u_form,
        #'csrf_token' : csrf.get_token(request),
    }
    return render(request, 'edit.html', context)


def search_user(request):
    if request.method == 'POST':
        query = request.POST['query']
        accounts = User.objects.filter(username__icontains=query) or User.objects.filter(email__icontains=query)
        context = {
            'query': query,
            'accounts': accounts
        }
        return render(request, 'search_user.html', context)
    else:
        return render(request, 'search_user.html')


def friends_list(request):
    if request.user.is_authenticated:
        return render(request, 'friends_list.html')





