from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):

    context = {"nome": "Raimundo"}
    return render(request, template_name="index.html")