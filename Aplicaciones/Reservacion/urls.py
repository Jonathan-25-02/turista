from django.urls import path
from . import views
urlpatterns = [
    path('turista', views.turista),
    path('nuevoTurista', views.nuevoTurista),
    path('agregarTurista', views.agregarTurista),
    path('editarTurista/<int:id>', views.editarTurista),
    path('procesarEdicionTurista/<int:id>', views.procesarEdicionTurista),
    path('eliminarTurista/<int:id>', views.eliminarTurista),
    
    path('reservacion', views.reservacion),
    path('nuevaReservacion', views.nuevaReservacion),
    path('agregarReservacion', views.agregarReservacion),
    path('editarReservacion/<int:id>', views.editarReservacion),
    path('procesarEdicionReservacion/<int:id>', views.procesarEdicionReservacion),
    path('eliminarReservacion/<int:id>', views.eliminarReservacion),

]