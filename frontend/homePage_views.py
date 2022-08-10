from django.http import HttpResponse

# from django import settings


def index(request):
    # return HttpResponse("This is home page, welcome")
    return HttpResponse(str(settings.STATICFILES_DIRS))