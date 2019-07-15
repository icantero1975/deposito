from django.conf.urls import url, include
from ocra.views import index, Autoridadlist, AutoridadCreate, AutoridadUpdateView, AutoridadDeleteView
from ocra.views import remitelist, remiteCreate, remiteUpdateView, remiteDeleteView
from ocra.views import vigilantelist, vigilanteCreate, vigilanteUpdateView, vigilanteDeleteView
from ocra.views import grualist, gruaCreate, gruaUpdateView, gruaDeleteView
from ocra.views import dplist, dpCreate, dpUpdateView, dpDeleteView
from ocra.views import oficiolist, oficioCreate, oficioUpdateView
from ocra.views import vhlist, vhCreate, vhUpdateView
from ocra.views import dvlist, dvCreate, dvUpdateView,logout_view
from django.contrib.auth import login
from django.contrib.auth.views import LoginView








urlpatterns = [
    url(r'^$',LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^index/$', index, name= 'index'),
    url(r'^cerrar/$',logout_view,name='logout'),
    url(r'^listar_aut$', Autoridadlist.as_view(), name='autoridad_listar'),
    url(r'^crear_aut$', AutoridadCreate.as_view(), name='autoridad_crear'),
    url(r'^editar_aut/(?P<pk>\d+)/$', AutoridadUpdateView.as_view(), name='autoridad_editar'),
    url(r'^eliminar_aut/(?P<pk>\d+)/$', AutoridadDeleteView.as_view(), name='autoridad_eliminar'),
    url(r'^listar_rm$', remitelist.as_view(), name='remite_listar'),
    url(r'^crear_rm$', remiteCreate.as_view(), name='remite_crear'),
    url(r'^editar_rm/(?P<pk>\d+)/$', remiteUpdateView.as_view(), name='remite_editar'),
    url(r'^eliminar_rm/(?P<pk>\d+)/$', remiteDeleteView.as_view(), name='remite_eliminar'),
    url(r'^listar_vg$', vigilantelist.as_view(), name='vigilante_listar'),
    url(r'^crear_vg$', vigilanteCreate.as_view(), name='vigilante_crear'),
    url(r'^editar_vg/(?P<pk>\d+)/$', vigilanteUpdateView.as_view(), name='vigilante_editar'),
    url(r'^eliminar_vg/(?P<pk>\d+)/$', vigilanteDeleteView.as_view(), name='vigilante_eliminar'),
    url(r'^listar_grua$', grualist.as_view(), name='grua_listar'),
    url(r'^crear_grua$', gruaCreate.as_view(), name='grua_crear'),
    url(r'^editar_grua/(?P<pk>\d+)/$', gruaUpdateView.as_view(), name='grua_editar'),
    url(r'^eliminar_grua/(?P<pk>\d+)/$', gruaDeleteView.as_view(), name='grua_eliminar'),
    url(r'^listar_deposito$', dplist.as_view(), name='deposito_listar'),
    url(r'^crear_deposito$', dpCreate.as_view(), name='deposito_crear'),
    url(r'^editar_deposito/(?P<pk>\d+)/$', dpUpdateView.as_view(), name='deposito_editar'),
    url(r'^eliminar_deposito/(?P<pk>\d+)/$', dpDeleteView.as_view(), name='deposito_eliminar'),
    url(r'^listar_oficio$', oficiolist.as_view(), name='oficio_listar'),
    url(r'^crear_oficio$', oficioCreate.as_view(), name='oficio_crear'),
    url(r'^editar_oficio/(?P<pk>\d+)/$', oficioUpdateView.as_view(), name='oficio_editar'),
    url(r'^listar_vehiculo$', vhlist.as_view(), name='vehiculo_listar'),
    url(r'^crear_vehiculo$', vhCreate.as_view(), name='vehiculo_crear'),
    url(r'^editar_vehiculo/(?P<pk>\d+)/$', vhUpdateView.as_view(), name='vehiculo_editar'),
    url(r'^listar_dev$', dvlist.as_view(), name='devolucion_listar'),
    url(r'^crear_dev$', dvCreate.as_view(), name='devolucion_crear'),
    url(r'^editar_dev/(?P<pk>\d+)/$', dvUpdateView.as_view(), name='devolucion_editar'),
    
    ]


