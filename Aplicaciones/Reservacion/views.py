from django.shortcuts import render, redirect
from .models import Turista, Reservacion
from django.contrib import messages


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
    logo=request.FILES.get("logo")

    Turista.objects.create(
        nombre=nombre,
        apellido=apellido,
        correo=correo,
        telefono=telefono,
        nacionalidad=nacionalidad,
        fecha_nacimiento=fecha_nacimiento,
        logo=logo
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
    turista.logo=request.FILES.get("logo")
    turista.save()
    messages.success(request, "Turista actualizado exitosamente")
    return redirect('/turista')

def eliminarTurista(request, id):
    turista = Turista.objects.get(id_turista=id)
    turista.delete()
    messages.success(request, "Turista eliminado exitosamente")
    return redirect('/turista')




def reservacion(request):
    listadoReservacion = Reservacion.objects.all()
    return render(request, "reservacion.html", {'reservaciones': listadoReservacion})

def nuevaReservacion(request):
    turistas = Turista.objects.all()
    return render(request, "nuevaReservacion.html", {'turistas': turistas})

def agregarReservacion(request):
    turista_id = request.POST["turista"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_fin"]
    destino = request.POST["destino"]
    monto = request.POST["monto"]
    estado = request.POST["estado"]
    logo=request.FILES.get("logo")

    turista = Turista.objects.get(id_turista=turista_id)

    Reservacion.objects.create(
        turista=turista,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        destino=destino,
        monto=monto,
        estado=estado,
        logo=logo
    )
    messages.success(request, "Reservación registrada exitosamente")
    return redirect('/reservacion')

def editarReservacion(request, id):
    reservacionEditar = Reservacion.objects.get(id_reservacion=id)
    turistas = Turista.objects.all()
    return render(request, "editarReservacion.html", {'reservacionEditar': reservacionEditar, 'turistas': turistas})

def procesarEdicionReservacion(request, id):
    reservacion = Reservacion.objects.get(id_reservacion=id)
    turista_id = request.POST["turista"]
    reservacion.turista = Turista.objects.get(id_turista=turista_id)
    reservacion.fecha_inicio = request.POST["fecha_inicio"]
    reservacion.fecha_fin = request.POST["fecha_fin"]
    reservacion.destino = request.POST["destino"]
    reservacion.monto = request.POST["monto"]
    reservacion.estado = request.POST["estado"]
    reservacion.logo = request.FILES.get("logo")
    reservacion.save()
    messages.success(request, "Reservación actualizada exitosamente")
    return redirect('/reservacion')

def eliminarReservacion(request, id):
    reservacion = Reservacion.objects.get(id_reservacion=id)
    reservacion.delete()
    messages.success(request, "Reservación eliminada exitosamente")
    return redirect('/reservacion')
