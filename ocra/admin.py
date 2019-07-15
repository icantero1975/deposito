from django.contrib import admin
from ocra.models import *
# Register your models here.


admin.site.register(remite)
admin.site.register(vigilante)
admin.site.register(grua)
admin.site.register(deposito)
admin.site.register(Oficio)
admin.site.register(vehiculo)
admin.site.register(devolucion)

#class adminautoridad(admin.ModelAdmin):
#	list_filter = ('adscripcion','cargo')
#    list_display = ('nombre_aut','adscripcion','cargo')
#    ordering = ('nombre_aut',)
#    search_fields = ('nombre_aut',)
#    fields = ['nombre_aut', ('adscripcion', 'cargo')]

#admin.site.register(Autoridad,adminautoridad)
# class adminaut(admin.ModelAdmin):
# 	fields = ['nombre_aut', ('adscripcion','cargo')]
# 	list_filter = ('adscripcion','cargo')
# 	ordering = ('nombre_aut',)
# 	search_fields = ('nombre_aut',)
# 	list_display = ('nombre_aut','adscripcion','cargo')

# admin.site.register(Autoridad,adminaut)


@admin.register(Autoridad) 
class autoridad(admin.ModelAdmin):
    list_filter = ('adscripcion','cargo')
    list_display = ('nombre_aut','adscripcion','cargo')
    ordering = ('nombre_aut',)
    search_fields = ('nombre_aut',)
    fields = ['nombre_aut', ('adscripcion', 'cargo')]
