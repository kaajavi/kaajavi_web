from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada
# Create your views here.
def home(request):
    context = RequestContext(request)
    #posts = Entrada.objects.all()
    posts = Entrada.objects.filter(published = True)
    return render_to_response('home.html', 
                              {'posts':posts},
                              context)

def ver_post(request, id_post):
    context = RequestContext(request)
    mi_post = Entrada.objects.get(id=id_post)
    return render_to_response('post.html', 
                              {'post':mi_post},
                              context)