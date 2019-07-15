from django import forms
from ocra.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class MpForm(forms.ModelForm):

    class Meta:
        model = Autoridad
        fields = [
            'nombre_aut',
            'cargo',
            'adscripcion',
        ]
        labels = {
            'nombre_aut':'Nombre del Responsable (Nombre, Apellido Paterno, Apellido Materno)',
            'cargo':'Cargo',
            'adscripcion':'Adscripción',
        }
        widgets = {
            'nombre_aut':forms.TextInput(attrs={'class':'form-control'}),
            'cargo':forms.TextInput(attrs={'class':'form-control'}),
            'adscripcion':forms.TextInput(attrs={'class': 'form-control'}),
        }

class remiteForm(forms.ModelForm):

    class Meta:
        model = remite
        fields = [
            'nombre_remite',
            'cargo_remite',
            'adscripcion_remite',
            'telefono',
            'tipo_autoridad',
        ]
        labels = {
            'nombre_remite':'Nombre del Remitente (Nombre, Apellido Paterno, Apellido Materno)',
            'cargo_remite':'Cargo del remitente',
            'adscripcion_remite':'Adscripción del remitente',
            'telefono':'Teléfono del Remitente',
            'tipo_autoridad': 'Tipo de Autoridad',
        }
        widgets = {
            'nombre_remite':forms.TextInput(attrs={'class':'form-control'}),
            'cargo_remite':forms.TextInput(attrs={'class':'form-control'}),
            'adscripcion_remite':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_autoridad':forms.Select(attrs={'class': 'form-control'}),
        }

class vigilanteForm(forms.ModelForm):

    class Meta:
        model = vigilante
        fields = [
            'nombre_vigilante',
            'cargo_vigilate',
            'expediente',
            'fecha_ingreso',
            
        ]
        labels = {
            'nombre_vigilante':'Nombre del vigilante (Nombre, Apellido Paterno, Apellido Materno)',
            'cargo_vigilate':'Cargo del vigilante',
            'expediente':'Número de expediente del vigilante ',
            'fecha_ingreso':'Fecha de Ingreso al Depósito de Vehículos',
        }
        widgets = {
            'nombre_vigilante':forms.TextInput(attrs={'class':'form-control'}),
            'cargo_vigilate':forms.TextInput(attrs={'class':'form-control'}),
            'expediente':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso':DateInput(),
            
        }
class vigilante1Form(forms.ModelForm):

    class Meta:
        model = vigilante
        fields = [
            'nombre_vigilante',
            'cargo_vigilate',
            'expediente',
            'fecha_ingreso',
            
        ]
        labels = {
            'nombre_vigilante':'Nombre del vigilante (Nombre, Apellido Paterno, Apellido Materno)',
            'cargo_vigilate':'Cargo del vigilante',
            'expediente':'Número de expediente del vigilante ',
            'fecha_ingreso':'Fecha de Ingreso al Depósito de Vehículos',
        }
        widgets = {
            'nombre_vigilante':forms.TextInput(attrs={'class':'form-control'}),
            'cargo_vigilate':forms.TextInput(attrs={'class':'form-control'}),
            'expediente':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso':forms.DateInput(attrs={'class': 'form-control'}),
        }

class gruaForm(forms.ModelForm):

    class Meta:
        model = grua
        fields = [
            'nombre_grua',
            'grua_tipo',
            'direccion_grua',
            'telefono_grua',
            
        ]
        labels = {
            'nombre_grua':'Razon social de las gruas',
            'grua_tipo':'Tipo de la grua',
            'direccion_grua':'Domicilio ',
            'telefono_grua':'Teléfono de la gruas',
        }
        widgets = {
            'nombre_grua':forms.TextInput(attrs={'class':'form-control'}),
            'grua_tipo':forms.Select(attrs={'class':'form-control'}),
            'direccion_grua':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_grua':forms.TextInput(attrs={'class': 'form-control'}),
        }

class depositoForm(forms.ModelForm):

    class Meta:
        model = deposito
        fields = [
            'nombre_deposito',
            'direccion_deposito',
            'fecha_funcion',
            'fecha_cierre',
            'responsable',
            'telefono_resp',
            
        ]
        labels = {
            'nombre_deposito':'Razon social del Depósito de Vehículos',
            'direccion_deposito':'Dirección del Depósito de Vehículos',
            'fecha_funcion':'Fecha de inicio de operaciones ',
            'fecha_cierre':'Fecha de cierre de operaciones',
            'responsable': 'Nombre del Responsable del Depósito',
            'telefono_resp': 'Teléfono del Responsable del Depósito',
        }
        widgets = {
            'nombre_deposito':forms.TextInput(attrs={'class':'form-control'}),
            'direccion_deposito':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_funcion' : DateInput(),
            'fecha_cierre' : DateInput(),
            'responsable':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_resp':forms.TextInput(attrs={'class': 'form-control'}),
        }
class deposito1Form(forms.ModelForm):

    class Meta:
        model = deposito
        fields = [
            'nombre_deposito',
            'direccion_deposito',
            'fecha_funcion',
            'fecha_cierre',
            'responsable',
            'telefono_resp',
            
        ]
        labels = {
            'nombre_deposito':'Razon social del Depósito de Vehículos',
            'direccion_deposito':'Dirección del Depósito de Vehículos',
            'fecha_funcion':'Fecha de inicio de operaciones ',
            'fecha_cierre':'Fecha de cierre de operaciones',
            'responsable': 'Nombre del Responsable del Depósito',
            'telefono_resp': 'Teléfono del Responsable del Depósito',
        }
        widgets = {
            'nombre_deposito':forms.TextInput(attrs={'class':'form-control'}),
            'direccion_deposito':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_funcion' : forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_cierre' : forms.DateInput(attrs={'class': 'form-control'}),
            'responsable':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_resp':forms.TextInput(attrs={'class': 'form-control'}),
        }

class oficioForm(forms.ModelForm):

    class Meta:
        model = Oficio
        fields = [
            'nombre_aut',
            'num_oficio',
            'fecha',
            'hora',
            'expediente',
            'numero_exp',
            'nombre_remite',
            'nombre_vigilante',

            
        ]
        labels = {
            'nombre_aut':'Elija una autoridad responsable',
            'num_oficio':'Número de Oficio',
            'fecha':'Fecha del Oficio',
            'hora':'Hora de Ingreso del Vehiculo',
            'expediente':'Tipo de Expediente',
            'numero_exp':'Numero del Expediente ejemplo: CDI. 258/2019/ZC',
            'nombre_remite':'Elija un remitente del Vehículo',
            'nombre_vigilante':'Elija un vigilante responsable',
        }
        widgets = {
            'nombre_aut':forms.Select(attrs={'class':'form-control'}),
            'num_oficio':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha' : DateInput(),
            'hora' :forms.TimeInput(attrs={'class':'form-control'}),
            'expediente': forms.Select(attrs={'class':'form-control'}),
            'numero_exp':forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_remite':forms.Select(attrs={'class':'form-control'}),
            'nombre_vigilante': forms.Select(attrs={'class':'form-control'}),
            
        }

class oficio1Form(forms.ModelForm):

    class Meta:
        model = Oficio
        fields = [
            'nombre_aut',
            'num_oficio',
            'fecha',
            'hora',
            'expediente',
            'numero_exp',
            'nombre_remite',
            'nombre_vigilante',

            
        ]
        labels = {
            'nombre_aut':'Elija una autoridad responsable',
            'num_oficio':'Número de Oficio',
            'fecha':'Fecha del Oficio',
            'hora':'Hora de Ingreso del Vehiculo',
            'expediente':'Tipo de Expediente',
            'numero_exp':'Numero del Expediente ejemplo: CDI. 258/2019/ZC',
            'nombre_remite':'Elija un remitente del Vehículo',
            'nombre_vigilante':'Elija un vigilante responsable',
        }
        widgets = {
            'nombre_aut':forms.Select(attrs={'class':'form-control'}),
            'num_oficio':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha' : forms.DateInput(attrs={'class': 'form-control'}),
            'hora' :forms.TimeInput(attrs={'class':'form-control'}),
            'expediente': forms.Select(attrs={'class':'form-control'}),
            'numero_exp':forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_remite':forms.Select(attrs={'class':'form-control'}),
            'nombre_vigilante': forms.Select(attrs={'class':'form-control'}),
            
        }

class vehiculoForm(forms.ModelForm):

    class Meta:
        model = vehiculo
        fields = [
            'Num_expediente',
            'num_oficio',
            'nombre_aut',
            'nombre_grua',
            'nombre_deposito',
            'fecha_ingreso',
            'marca',
            'tipo',
            'color',
            'modelo',
            'placa',
            'estado',
            'serie',
            'motor',
            'tipo_auto',
            'estatus',
            'fleje',
            'folio_fleje',
            'motivo',
            'procedencia',
            'estado_veh',
            'llaves',
            'funciona',
            'sellos',
            'valores',
            'especifique',
            'observacion',
            'Sasca',

        ]
        labels = {
            'Num_expediente':'Ingrese el número de expediente p/e: 170/R/2019',
            'num_oficio':'Elija un número de Oficio',
            'nombre_aut':'Elija la autoridad que remite el Vehículo',
            'nombre_grua':'Elija la grua que traslado el Vehículo',
            'nombre_deposito':'Elija el depósito donde sera resguardado',
            'fecha_ingreso':'Fecha de ingreso del Vehículo',
            'marca':'Marca del Vehículo p/e: Nissan',
            'tipo': 'Tipo del Vehículo p/e: Tsuru',
            'color':'Color del Vehículo',
            'modelo': 'Año del Vehículo',
            'placa': 'Número de la placa de circulación',
            'estado': 'Estado de Origen de las placa de circulación',
            'serie': 'Serie o número de VIN del Vehículo',
            'motor': 'Número de Motor del Vehículo',
            'tipo_auto':'Clase del Vehículo',
            'estatus':'Estatus del Vehículo',
            'fleje':'Contiene Fleje',
            'folio_fleje':'Folio del Fleje',
            'motivo': 'Motivo del Ingreso del Vehículo',
            'procedencia':'De Donde procede el Vehículo',
            'estado_veh': 'Estado de Conservación del Vehículo',
            'llaves': 'Tiene llaves el vehículo',
            'funciona':'Funciona el Vehículo',
            'sellos':'Tiene sellos',
            'valores':'Tiene Valores',
            'especifique':'Especifique los valores',
            'observacion': 'Observaciones adicionales',
            'Sasca':'Número de Sasca',
        }
        widgets = {

            'Num_expediente':forms.TextInput(attrs={'class':'form-control'}),
            'num_oficio':forms.Select(attrs={'class':'form-control'}),
            'nombre_aut':forms.Select(attrs={'class':'form-control'}),
            'nombre_grua':forms.Select(attrs={'class':'form-control'}),
            'nombre_deposito':forms.Select(attrs={'class':'form-control'}),
            'fecha_ingreso':DateInput(),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.TextInput(attrs={'class':'form-control'}),
            'color':forms.TextInput(attrs={'class':'form-control'}),
            'modelo':forms.TextInput(attrs={'class':'form-control'}),
            'placa':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'}),
            'serie':forms.TextInput(attrs={'class':'form-control'}),
            'motor':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_auto':forms.Select(attrs={'class':'form-control'}),
            'estatus':forms.Select(attrs={'class':'form-control'}),
            'fleje':forms.Select(attrs={'class':'form-control'}),
            'folio_fleje':forms.TextInput(attrs={'class':'form-control'}),
            'motivo':forms.Select(attrs={'class':'form-control'}),
            'procedencia':forms.Select(attrs={'class':'form-control'}),
            'estado_veh':forms.Select(attrs={'class':'form-control'}),
            'llaves':forms.Select(attrs={'class':'form-control'}),
            'funciona':forms.Select(attrs={'class':'form-control'}),
            'sellos':forms.Select(attrs={'class':'form-control'}),
            'valores':forms.Select(attrs={'class':'form-control'}),
            'especifique':forms.Textarea(attrs={'class':'form-control'}),
            'observacion':forms.Textarea(attrs={'class':'form-control'}),
            'Sasca':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class vehiculo1Form(forms.ModelForm):

    class Meta:
        model = vehiculo
        fields = [
            'Num_expediente',
            'num_oficio',
            'nombre_aut',
            'nombre_grua',
            'nombre_deposito',
            'fecha_ingreso',
            'marca',
            'tipo',
            'color',
            'modelo',
            'placa',
            'estado',
            'serie',
            'motor',
            'tipo_auto',
            'estatus',
            'fleje',
            'folio_fleje',
            'motivo',
            'procedencia',
            'estado_veh',
            'llaves',
            'funciona',
            'sellos',
            'valores',
            'especifique',
            'observacion',
            'Sasca',

        ]
        labels = {
            'Num_expediente':'Ingrese el número de expediente p/e: 170/R/2019',
            'num_oficio':'Elija un número de Oficio',
            'nombre_aut':'Elija la autoridad que remite el Vehículo',
            'nombre_grua':'Elija la grua que traslado el Vehículo',
            'nombre_deposito':'Elija el depósito donde sera resguardado',
            'fecha_ingreso':'Fecha de ingreso del Vehículo',
            'marca':'Marca del Vehículo p/e: Nissan',
            'tipo': 'Tipo del Vehículo p/e: Tsuru',
            'color':'Color del Vehículo',
            'modelo': 'Año del Vehículo',
            'placa': 'Número de la placa de circulación',
            'estado': 'Estado de Origen de las placa de circulación',
            'serie': 'Serie o número de VIN del Vehículo',
            'motor': 'Número de Motor del Vehículo',
            'tipo_auto':'Clase del Vehículo',
            'estatus':'Estatus del Vehículo',
            'fleje':'Contiene Fleje',
            'folio_fleje':'Folio del Fleje',
            'motivo': 'Motivo del Ingreso del Vehículo',
            'procedencia':'De Donde procede el Vehículo',
            'estado_veh': 'Estado de Conservación del Vehículo',
            'llaves': 'Tiene llaves el vehículo',
            'funciona':'Funciona el Vehículo',
            'sellos':'Tiene sellos',
            'valores':'Tiene Valores',
            'especifique':'Especifique los valores',
            'observacion': 'Observaciones adicionales',
            'Sasca':'Número de Sasca',
        }
        widgets = {

            'Num_expediente':forms.TextInput(attrs={'class':'form-control'}),
            'num_oficio':forms.Select(attrs={'class':'form-control'}),
            'nombre_aut':forms.Select(attrs={'class':'form-control'}),
            'nombre_grua':forms.Select(attrs={'class':'form-control'}),
            'nombre_deposito':forms.Select(attrs={'class':'form-control'}),
            'fecha_ingreso':forms.DateInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.TextInput(attrs={'class':'form-control'}),
            'color':forms.TextInput(attrs={'class':'form-control'}),
            'modelo':forms.TextInput(attrs={'class':'form-control'}),
            'placa':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'}),
            'serie':forms.TextInput(attrs={'class':'form-control'}),
            'motor':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_auto':forms.Select(attrs={'class':'form-control'}),
            'estatus':forms.Select(attrs={'class':'form-control'}),
            'fleje':forms.Select(attrs={'class':'form-control'}),
            'folio_fleje':forms.TextInput(attrs={'class':'form-control'}),
            'motivo':forms.Select(attrs={'class':'form-control'}),
            'procedencia':forms.Select(attrs={'class':'form-control'}),
            'estado_veh':forms.Select(attrs={'class':'form-control'}),
            'llaves':forms.Select(attrs={'class':'form-control'}),
            'funciona':forms.Select(attrs={'class':'form-control'}),
            'sellos':forms.Select(attrs={'class':'form-control'}),
            'valores':forms.Select(attrs={'class':'form-control'}),
            'especifique':forms.Textarea(attrs={'class':'form-control'}),
            'observacion':forms.Textarea(attrs={'class':'form-control'}),
            'Sasca':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class devolucionForm(forms.ModelForm):

    class Meta:
        model = devolucion
        fields = [
            'Num_expediente',
            'nombre_aut',
            'num_oficio',
            'fecha_oficio',
            'fecha_entrega',
            'hora_entrega',
            'entrega',
            'nombre_propietario',
            'identificacion',
            'numero_iden',
            'telefono_usuario',
            'correo',
            'dias',
            'cobro',
            'descuento',
            'cobro_grua',
        ]
        labels = {
            'Num_expediente':'Expediente del vehículo',
            'nombre_aut':'Nombre de la Autoridad',
            'num_oficio':'Número de Oficio de solicitud de devolución',
            'fecha_oficio':'Fecha Oficio',
            'fecha_entrega':'Fecha de Entrega',
            'hora_entrega':'Hora de Entrega',
            'entrega':'Autoriza Egreso',
            'nombre_propietario':'Nombre del Propietario',
            'identificacion':'Identificación del Propietario',
            'numero_iden':'Número de Identificación',
            'telefono_usuario':'Teléfono del Propietario',
            'correo':'Correo Electronico del Propietario',
            'dias':'Dias de Piso',
            'cobro':'Cantidad a Cobrar',
            'descuento':'Descuento',
            'cobro_grua':'Cobro por arrastre de Grua',
        }
        widgets = {
            'Num_expediente': forms.Select(attrs={'class':'form-control'}),
            'nombre_aut': forms.Select(attrs={'class':'form-control'}),
            'num_oficio':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_oficio': DateInput(),
            'fecha_entrega': DateInput(),
            'hora_entrega':forms.TimeInput(attrs={'class':'form-control'}),
            'entrega':forms.TextInput(attrs={'class':'form-control'}),
            'nombre_propietario':forms.TextInput(attrs={'class':'form-control'}),
            'identificacion':forms.Select(attrs={'class':'form-control'}),
            'numero_iden':forms.TextInput(attrs={'class':'form-control'}),
            'telefono_usuario':forms.TextInput(attrs={'class':'form-control'}),
            'correo':forms.TextInput(attrs={'class':'form-control'}),
            'dias':forms.NumberInput(attrs={'class':'form-control'}),
            'cobro':forms.NumberInput(attrs={'class':'form-control'}),
            'descuento':forms.Select(attrs={'class':'form-control'}),
            'cobro_grua':forms.NumberInput(attrs={'class':'form-control'}),
            
        }


