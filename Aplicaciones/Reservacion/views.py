from django.shortcuts import render,redirect
from .models import Turista, Reservacion
from django.contrib import messages

# Create your views here.
def turista(request):
    listadoTurista = Turista.objects.all()
    return render(request, "turista.html", {'turistas': listadoTurista})

def nuevoTurista(request):
    return render(request, "nuevoTurista.html")

def agregarTurista(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    correo = request.POST["correo"]
    telefono = request.POST["telefono"]
    nacionalidad = request.POST["nacionalidad"]
    fecha_nacimiento = request.POST.get("fecha_nacimiento", None)

    Turista.objects.create(
        nombre=nombre,
        apellido=apellido,
        correo=correo,
        telefono=telefono,
        nacionalidad=nacionalidad,
        fecha_nacimiento=fecha_nacimiento
    )
    messages.success(request, "Turista registrado exitosamente")
    return redirect('/turista')

def editarTurista(request, id):
    turistaEditar = Turista.objects.get(id_turista=id)
    return render(request, "editarTurista.html", {'turistaEditar': turistaEditar})

def procesarEdicionTurista(request, id):
    turista = Turista.objects.get(id_turista=id)
    turista.nombre = request.POST["nombre"]
    turista.apellido = request.POST["apellido"]
    turista.correo = request.POST["correo"]
    turista.telefono = request.POST["telefono"]
    turista.nacionalidad = request.POST["nacionalidad"]
    turista.fecha_nacimiento = request.POST.get("fecha_nacimiento", None)
    turista.save()
    messages.success(request, "Turista actualizado exitosamente")
    return redirect('/turista')

def eliminarTurista(request, id):
    turista = Turista.objects.get(id_turista=id)
    turista.delete()
    messages.success(request, "Turista eliminado exitosamente")
    return redirect('/turista')