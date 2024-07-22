
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name = "index"),
    path('saludo/', views.saludo, name = "saludo"),
    path('persona/', views.personas, name='persona'),
    path('agregar_persona/', views.agregar_persona, name='agregar_persona'),
    path('eliminar_persona/<int:id>/', views.eliminar_persona, name='eliminar_persona'),
    path('editar_persona/<int:id>/', views.editar_persona, name='editar_persona'),

]
