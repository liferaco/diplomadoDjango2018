from django import forms
from pagina.models import producto

class productoForm(forms.ModelForm):

	class Meta:
		model = producto

		fields = [
		'idMarca',
		'codigo',
		'nombre',
		'tipo',
		'costo',
		]

		labels = {
		'idMarca' : 'Marca',
		'codigo' : 'Codigo',
		'nombre' : 'Nombre',
		'tipo' : 'Tipo',
		'costo' : 'Costo',
		}

		widgets = {
		'idMarca' : forms.Select(attrs = {'class' : 'form-control'}),
		'codigo' : forms.TextInput(attrs = {'class' : 'form-control'}),
		'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
		'tipo' : forms.TextInput(attrs = {'class' : 'form-control'}),
		'costo' : forms.TextInput(attrs = {'class' : 'form-control'}),
		}