from django.shortcuts import render

def index(request):
    print("results: ")
    return render(request, "course/home.html")

def about(request):
    print("results: ")
    return render(request, "course/about.html")

def contact(request):
    print("results: ")
    return render(request, "course/contact.html")