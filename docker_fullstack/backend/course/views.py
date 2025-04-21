from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home Page</h1>")