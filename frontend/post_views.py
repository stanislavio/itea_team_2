from django.shortcuts import render, redirect


from .forms import CreateSocialPostForm, CreateTrainingPostForm

from db.models import SocialPost, TrainingPost

import datetime
# import dateutil

def create_social_post(request):
    form = CreateSocialPostForm(initial={"post_is_private": True})
    
    if request.method == "POST":
        form = CreateSocialPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('view_social_post', post_id=new_post.id)
    context = {
        'form' : form,
    }
    return render(request, 'create_post_page.html', context)

def create_training_post(request):
    form = CreateTrainingPostForm(initial={"post_is_private": True})
    if request.method == "POST":
        form = CreateTrainingPostForm(request.POST)
        if form.is_valid():
            new_training_post = form.save(commit=False)
            new_training_post.author = request.user
            new_training_post.save()
            return redirect('view_training_post', post_id=new_training_post.id)

    context = {
        'form' : form,
    }
    return render(request, 'create_training_post.html', context)

def view_social_post(request, post_id):
    post_to_show = SocialPost.objects.get(id=post_id)
    context = {
        'post' : post_to_show,
    }
    return render(request, 'view_social_post.html', context)

def view_training_post(request, post_id):
    return render(request, 'view_training_post.html')
