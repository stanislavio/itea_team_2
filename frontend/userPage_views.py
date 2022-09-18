from django.shortcuts import render, redirect
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from db.models import User
from django.middleware import csrf


def friends_list(request):
    return render(request, 'friends_list.html')


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
                'hide_phone': user.hide_phone
            }
            return render(request, 'user_profile.html', context)
        if request.user.id != user_id:
            user = request.user.id
            account = User.objects.get(pk=int(user_id))
            context = {
                'user': user,
                'username': account.username,
                'email': account.email,
                'photo': account.photo,
                'phone': account.phone,
                'short_bio': account.short_bio,
                'hide_email': account.hide_email,
                'hide_phone': account.hide_phone
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


def friends_list(request):
    return render(request, 'friends_list.html')


def change_friend_status(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        User.add_friend(request.user, friend)
    elif operation == 'remove':
        User.remove_friend(request.user, friend)
    return redirect('friends_list')

# @login_required
# def send_friend_request(request, user_id):
#     from_user = request.user
#     to_user = User.objects.get(id=user_id)
#     friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
#     return render(request, 'friends_list.html')
#
#
# @login_required
# def accept_friend_request(request, request_id):
#     friend_request = FriendRequest.objects.get(id=request_id)
#     if friend_request.to_user == request.user:
#         friend_request.to_user.friends.add(friend_request.from_user)
#         friend_request.from_user.friends.add(friend_request.to_user)
#         friend_request.delete()
#         return HttpResponse('friend request accepted')
#     else:
#         return HttpResponse('friend request not accepted')
