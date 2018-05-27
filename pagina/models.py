from django.db import models

# Create your models here.
class marca(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class producto(models.Model):
	idMarca = models.ForeignKey(marca, on_delete=models.CASCADE)
	codigo = models.CharField(max_length=50,unique=True)
	nombre = models.CharField(max_length=100)
	tipo = models.CharField(max_length=50,null=True,blank=True)
	costo = models.DecimalField(max_digits=14, decimal_places=2)

class stock(models.Model):
	idProducto = models.ForeignKey(producto, on_delete=models.CASCADE)
	total= models.DecimalField(max_digits=14, decimal_places=2)

class movimiento(models.Model):
	tipoMovimiento = (('E', 'entrada'),('S', 'salida'))
	idProducto = models.OneToOneField(producto, on_delete=models.CASCADE)
	fecha = models.DateField()
	nomMovimiento = models.CharField(max_length=1,choices=tipoMovimiento,default='E')
	cantidad = models.IntegerField()

