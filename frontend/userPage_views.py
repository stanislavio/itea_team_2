from django.shortcuts import render, redirect
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from db.models import User, Friend


def user_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'user_profile.html', args)


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
        'u_form': u_form
    }
    return render(request, 'edit.html', context)


def friends_list(request, *args, **kwargs):
    users = User.objects.exclude(id=request.user.id)
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()
    args = {'users': users, 'friends': friends}
    return render(request, 'friends_list.html', args)


def change_friend_status(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.add_friend(request.user, friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, friend)
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
