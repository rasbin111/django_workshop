
from django.urls import path
from course import views

urlpatterns = [
    path('', views.index, name="home-page"),
    path('about/', views.about, name="about-page"),
    path('contact/', views.contact, name="contact-page"),
]