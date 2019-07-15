from django.shortcuts import render
from django.urls import reverse_lazy
from ocra.models import *
from ocra.form import MpForm, remiteForm, vigilanteForm,vigilante1Form, gruaForm, depositoForm,oficioForm, oficio1Form,deposito1Form,vehiculoForm,vehiculo1Form,devolucionForm
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.contrib.auth import logout
   
# Create your views here.

def logout_view(request):
    logout(request)
    return render(request,'login.html')
    # Redirect to a success page.

def index(request):
    return render(request,'index.html')


class Autoridadlist(ListView):
	model = Autoridad
	template_name = 'mp_list.html'
	context_object_name = 'autoridad'
	

class AutoridadCreate(CreateView):
	model = Autoridad
	form_class = MpForm
	template_name = 'mp_form.html'
	success_url = reverse_lazy('autoridad_listar')

class AutoridadUpdateView(UpdateView):
	model = Autoridad
	form_class = MpForm
	template_name = 'mp_form.html'
	success_url = reverse_lazy('autoridad_listar')

class AutoridadDeleteView(DeleteView):
	model = Autoridad
	template_name = 'mp_delete.html'
	success_url = reverse_lazy('autoridad_listar')

# clases para el modelo de datos remite

class remitelist(ListView):
	model = remite
	template_name = 'rm_list.html'
	context_object_name = 'remitente'
	

class remiteCreate(CreateView):
	model = remite
	form_class = remiteForm
	template_name = 'rm_form.html'
	success_url = reverse_lazy('remite_listar')

class remiteUpdateView(UpdateView):
	model = remite
	form_class = remiteForm
	template_name = 'rm_form.html'
	success_url = reverse_lazy('remite_listar')

class remiteDeleteView(DeleteView):
	model = remite
	template_name = 'rm_delete.html'
	success_url = reverse_lazy('remite_listar')

# clases para el modelo de datos vigilante

class vigilantelist(ListView):
	model = vigilante
	template_name = 'vg_list.html'
	context_object_name = 'vigilantes'
	

class vigilanteCreate(CreateView):
	model = vigilante
	form_class = vigilanteForm
	template_name = 'vg_form.html'
	success_url = reverse_lazy('vigilante_listar')

class vigilanteUpdateView(UpdateView):
	model = vigilante
	form_class = vigilante1Form
	template_name = 'vg_form.html'
	success_url = reverse_lazy('vigilante_listar')

class vigilanteDeleteView(DeleteView):
	model = vigilante
	template_name = 'vg_delete.html'
	success_url = reverse_lazy('vigilante_listar')

# clases para el modelo de datos grua

class grualist(ListView):
	model = grua
	template_name = 'grua_list.html'
	context_object_name = 'gruas'
	

class gruaCreate(CreateView):
	model = grua
	form_class = gruaForm
	template_name = 'grua_form.html'
	success_url = reverse_lazy('grua_listar')

class gruaUpdateView(UpdateView):
	model = grua
	form_class = gruaForm
	template_name = 'grua_form.html'
	success_url = reverse_lazy('grua_listar')

class gruaDeleteView(DeleteView):
	model = grua
	template_name = 'grua_delete.html'
	success_url = reverse_lazy('grua_listar')

# clases para el modelo de datos deposito

class dplist(ListView):
	model = deposito
	template_name = 'dp_list.html'
	context_object_name = 'depositos'
	

class dpCreate(CreateView):
	model = deposito
	form_class = depositoForm
	template_name = 'dp_form.html'
	success_url = reverse_lazy('deposito_listar')

class dpUpdateView(UpdateView):
	model = deposito
	form_class = deposito1Form
	template_name = 'dp_form.html'
	success_url = reverse_lazy('deposito_listar')

class dpDeleteView(DeleteView):
	model = deposito
	template_name = 'dp_delete.html'
	success_url = reverse_lazy('deposito_listar')

# clases para el modelo de datos oficio

class oficiolist(ListView):
	model = Oficio
	template_name = 'oficio_list.html'
	context_object_name = 'oficios'
	

class oficioCreate(CreateView):
	model = Oficio
	form_class = oficioForm
	template_name = 'oficio_form.html'
	success_url = reverse_lazy('oficio_listar')

class oficioUpdateView(UpdateView):
	model = Oficio
	form_class = oficio1Form
	template_name = 'oficio_form.html'
	success_url = reverse_lazy('oficio_listar')

# clases para el modelo de datos vehiculo

class vhlist(ListView):
	model = vehiculo
	template_name = 'vh_list.html'
	context_object_name = 'vehiculos'
	

class vhCreate(CreateView):
	model = vehiculo
	form_class = vehiculoForm
	template_name = 'vh_form.html'
	success_url = reverse_lazy('vehiculo_listar')

class vhUpdateView(UpdateView):
	model = vehiculo
	form_class = vehiculo1Form
	template_name = 'vh_form.html'
	success_url = reverse_lazy('vehiculo_listar')

# clases para el modelo de datos devolucion

class dvlist(ListView):
	model = devolucion
	template_name = 'dv_list.html'
	context_object_name = 'devoluciones'
	

class dvCreate(CreateView):
	model = devolucion
	form_class = devolucionForm
	template_name = 'dv_form.html'
	success_url = reverse_lazy('devolucion_listar')

class dvUpdateView(UpdateView):
	model = devolucion
	form_class = devolucionForm
	template_name = 'dv_form.html'
	success_url = reverse_lazy('devolucion_listar')







