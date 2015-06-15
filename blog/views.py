from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada, Contacto
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

def contact(request):
    context = RequestContext(request)
    enviado = "No se envio"
    if request.method == 'POST':
        enviado="Entro al post, por lo menos"
        nombre= request.POST['nombre']
        celu= request.POST['celu']
        mail= request.POST['mail']
        mensaje= request.POST['mensaje']
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.celu = celu
        contacto.mail = mail
        contacto.mensaje = mensaje
        contacto.save()
        
        
        
    return render_to_response('contact.html', 
                              {'enviado':enviado},
                              context)