from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada
# Create your views here.
def home(request):
    context = RequestContext(request)
    mandar="Son unos salames"
    numeros = [23,45,67,86,43]
    posts = Entrada.objects.all()
    return render_to_response('home.html', 
                              {'algo':mandar,
                              'num':numeros,
                              'posts':posts},
                              context)

def ver_post(request, id_post):
    context = RequestContext(request)
    post = Entrada.objects.get(id=id_post)
    return render_to_response('post.html', 
                              {'post':post},
                              context)