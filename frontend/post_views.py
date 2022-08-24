from django.shortcuts import render, redirect


from .forms import CreatePostForm

def create_post(request):
    form = CreatePostForm(initial={"post_is_private": True})
    
    if request.method == "POST":
        print(request.POST)
        
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('index')

    context = {
        'form' : form,
    }


    return render(request, 'create_post_page.html', context)