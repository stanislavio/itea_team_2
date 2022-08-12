from django.shortcuts import render


def profile(request):
    return render(request, 'user_page.html')

def test_base(request):
    return render(request, 'base.html')