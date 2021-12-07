from django.db import models

class Producto(models.Model):
	nombre = models.CharField(max_length=255)
	precio = models.DecimalField(max_digits=9, decimal_places=2)

	class Meta:
		db_table="productos"

	def __str__(self):
		return self.nombre
