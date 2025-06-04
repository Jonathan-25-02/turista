from django.urls import path
from . import views
urlpatterns = [
    path('', views.home)
    # Aquí puedes agregar más rutas según sea necesario
]