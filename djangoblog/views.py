from django.http import HttpResponse

def homePage(request):
    return HttpResponse('Home')

def about(request):
    return HttpResponse('About')