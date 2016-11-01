from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the pariksani index.")

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

