from django.urls import path 

from . import views

app_name = "productos"

urlpatterns = [
	path("Detalle/", views.detalle, name="detalle"),
	
	# Admin
	path("Admin/Listar/", views.ListarAdmin.as_view(), name="admin_listar"),
	path("Admin/Nuevo/", views.NuevoAdmin.as_view(), name="admin_nuevo"),
	path("Admin/Editar/<int:pk>/", views.EditarAdmin.as_view(), name="admin_editar"),

]