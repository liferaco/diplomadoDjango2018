from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from pagina.forms import productoForm
from pagina.models import producto,marca

from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

# Create your views here.
def index(request):
	return render(request,'pagina/index.html')

def producto_view(request):
	if request.method == 'POST':
		form = productoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('pagina:index')
	else:
		form = productoForm()
	return render(request,'pagina/productoForm.html',{'form': form})

def producto_list(request):

	productos = producto.objects.all()
	contexto = {'productosContex':productos}

	return render(request,'pagina/productoList.html',contexto)

def producto_update(request,idProducto):

	productos = producto.objects.get(id=idProducto)
	if request.method=='GET':
		form= productoForm(instance=productos)
	else:
		form=productoForm(request.POST,instance=productos)
		if form.is_valid():
			form.save()
		return redirect('pagina:producto_listar')
	return render(request,'pagina/productoForm.html',{'form':form})


def producto_delete(request,idProducto):
	productos = producto.objects.get(id=idProducto)
	if request.method=='POST':
		productos.delete()
		return redirect('pagina:producto_listar')
	return render(request,'pagina/productoDelete.html',{'productos':productos})

class productoList(ListView):
	model = producto
	second_model = marca
	template_name = 'pagina/productoList.html'

	def get_context_data(self, **kwargs):
		context = super(productoList,self).get_context_data(**kwargs)
		context['productosContex'] = producto.objects.all()
		context['marcasContex'] = marca.objects.all()
		return context

class productoFiltrar(ListView):
	model = producto
	second_model = marca
	template_name = 'pagina/productoList.html'

	def get_queryset (self, **kwargs):
		a = self.kwargs['idMarca']
		return producto.objects.filter(idMarca=a)

	def get_context_data(self, **kwargs):
		context = super(productoFiltrar,self).get_context_data(**kwargs)
		context['productosContex'] = producto.objects.all()
		context['marcasContex'] = marca.objects.all()
		return context

class productoCreate(CreateView):
	model = producto
	form_class = productoForm
	template_name = 'pagina/productoForm.html'
	success_url = reverse_lazy('pagina:producto_listar')

class productoUpdate(UpdateView):
	model = producto
	form_class = productoForm
	template_name = 'pagina/productoForm.html'
	success_url = reverse_lazy('pagina:producto_listar')

class productoDelete(DeleteView):
	model = producto
	template_name = 'pagina/productoDelete.html'
	success_url = reverse_lazy('pagina:producto_listar')

class ReporteProductosPDF(View):
	
	def cabecera(self,pdf):
		#Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
		archivo_imagen = settings.MEDIA_ROOT+'/imagenes/carro.png'
		#Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
		pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
		#Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
		pdf.setFont("Helvetica", 16)
		#Dibujamos una cadena en la ubicación X,Y especificada
		pdf.drawString(230, 790, u"CASA DEL REPUESTO")
		pdf.setFont("Helvetica", 14)
		pdf.drawString(224, 770, u"REPORTE DE PRODUCTOS")

	def get(self, request, *args, **kwargs):
		#Indicamos el tipo de contenido a devolver, en este caso un pdf
		response = HttpResponse(content_type='application/pdf')
		#La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
		buffer = BytesIO()
		#Canvas nos permite hacer el reporte con coordenadas X y Y
		pdf = canvas.Canvas(buffer)
		#Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
		self.cabecera(pdf)
		y = 600
		self.tabla(pdf, y)
		#Con show page hacemos un corte de página para pasar a la siguiente
		pdf.showPage()
		pdf.save()
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response

	def tabla(self,pdf,y):
		#Creamos una tupla de encabezados para neustra tabla
		encabezados = ('N', 'Codigo', 'Nombre', 'Tipo','Costo','Marca')
		#Creamos una lista de tuplas que van a contener a las personas
		detalles = [(producto.id, producto.codigo, producto.nombre, producto.tipo,producto.costo,producto.idMarca) for producto in producto.objects.all()]
		#Establecemos el tamaño de cada una de las columnas de la tabla
		detalle_orden = Table([encabezados] + detalles, colWidths=[1 * cm, 3 * cm, 4 * cm, 2 * cm, 4 * cm, 3 * cm])
		#Aplicamos estilos a las celdas de la tabla
		detalle_orden.setStyle(TableStyle(
		[
			#La primera fila(encabezados) va a estar centrada
			('ALIGN',(0,0),(3,0),'CENTER'),
			#Los bordes de todas las celdas serán de color negro y con un grosor de 1
			('GRID', (0, 0), (-1, -1), 1, colors.black),
			#El tamaño de las letras de cada una de las celdas será de 10
			('FONTSIZE', (0, 0), (-1, -1), 10),
			]
		))
		#Establecemos el tamaño de la hoja que ocupará la tabla
		detalle_orden.wrapOn(pdf, 800, 600)
		#Definimos la coordenada donde se dibujará la tabla
		detalle_orden.drawOn(pdf, 60,y)



