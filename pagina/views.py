from django.shortcuts import render,redirect
from django.http import HttpResponse
from pagina.forms import productoForm
from pagina.models import producto


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
	return render(request,'pagina/productoForm.html',{'form':form})

def producto_list(request):

	productos = producto.objects.all()
	contexto = {'productosContex':productos}

	return render(request,'pagina/productoList.html',contexto)