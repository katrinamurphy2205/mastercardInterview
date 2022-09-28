from django.http import HttpResponse

def homepageView(request):
    return HttpResponse('Hello World')
