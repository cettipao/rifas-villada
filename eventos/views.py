import os

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from config.settings import BASE_DIR
from .models import *
from .imageGenerator import genImage
import json
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404


# Create your views here.

def homeView(request):
    return render(request, "home.html", {})


def verRifa(request, id):
    rifa = Rifa.objects.get(id=id)
    nombreImagen = genImage(rifa.comprador, str(rifa.id), request.get_host(), str(rifa.id))
    msg = 'http://' + request.get_host() + '/static/rifas/' + "rifa.png"
    return redirect(msg)

def createView(request):
    #return render(request, "stopped.html", {})
    if request.method == "POST":
        vendedor = Vendedor.objects.get(id=request.POST.get("vendedor"))
        comprador = request.POST.get("comprador")
        rifa = Rifa.objects.create(vendedor=vendedor, comprador=comprador)
        nombreImagen = genImage(comprador, str(rifa.id), request.get_host(), str(rifa.id))
        msg = 'http://' + request.get_host() + '/static/rifas/' + "rifa.png"
        return redirect(msg)


    vendedores = Vendedor.objects.all().order_by("nombre")
    return render(request, "create.html", {"vendedores":vendedores})

def rifaView(request, id):
    rifa = get_object_or_404(Rifa, id=id)
    return render(request, "rifa.html", {"rifa":rifa, "host":request.get_host()})
