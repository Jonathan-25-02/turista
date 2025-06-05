from django.urls import path
from . import views
urlpatterns = [
    path('turista', views.turista),
    path('nuevoTurista', views.nuevoTurista),
    path('agregarTurista', views.agregarTurista),
    path('editarTurista/<int:id>', views.editarTurista),
    path('actualizarTurista/<int:id>', views.actualizarTurista),
    path('eliminarTurista/<int:id>', views.eliminarTurista),
    
    path('reservacion', views.reservacion),
    path('nuevaReservacion', views.nuevaReservacion),
    path('agregarReservacion', views.agregarReservacion),
    path('editarReservacion/<int:id>', views.editarReservacion),
    path('actualizarReservacion/<int:id>', views.actualizarReservacion),
    path('eliminarReservacion/<int:id>', views.eliminarReservacion),

]