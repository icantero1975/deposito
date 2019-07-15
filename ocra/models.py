from django.db import models

# Create your models here.

class Autoridad(models.Model):
	nombre_aut = models.CharField(max_length=50, help_text='Nombre Completo empezando por Nombre, Apellido Paterno, Apellido Materno')
	cargo = models.CharField(max_length=50, help_text='Cargo de la Autoridad')
	adscripcion =  models.CharField(max_length=100, help_text='Adscripción de la Autoridad')
	class Meta:
		ordering = ['nombre_aut']
		verbose_name = "Autoridad"
		verbose_name_plural= "Autoridades"
	def __str__(self):
		return '(%s) %s' %(self.id, self.nombre_aut)

class remite(models.Model):
	nombre_remite =  models.CharField(max_length=50, help_text='Nombre Completo empezando por Nombre, Apellido Paterno, Apellido Materno')
	cargo_remite = models.CharField(max_length=50, help_text='Cargo de la Autoridad que remite el vehículo')
	adscripcion_remite =  models.CharField(max_length=100, help_text='Adscripción de la Autoridad que remite el vehículo')
	telefono = models.CharField(max_length=10, help_text='número telefonico')
	clase_autoridad = (('PM', 'POLICIA MINISTERIAL'),
                    ('PE', 'POLICIA ESTATAL'),
                    ('PP', 'POLICIA MUNICIPAL'),
                    ('PF', 'POLICIA FEDERAL'),
                    ('O', 'OTRO')
                )
	tipo_autoridad = models.CharField(max_length=2, choices=clase_autoridad, default='PM',help_text='Elije una opción')
	
	class Meta:
		ordering = ['nombre_remite']
		verbose_name = "Remitente"
		verbose_name_plural= "Remitentes"
	def __str__(self):
		return '(%s) %s' % (self.id, self.nombre_remite)

class vigilante(models.Model):
	nombre_vigilante =  models.CharField(max_length=50, help_text='Nombre Completo empezando por Nombre, Apellido Paterno, Apellido Materno')
	cargo_vigilate = models.CharField(max_length=50, help_text='Cargo del Administrativo')
	expediente = models.CharField(max_length=10, help_text='número de expediente')
	fecha_ingreso = models.DateField(null=True, blank=True)
	
	class Meta:
		ordering = ['nombre_vigilante']
		verbose_name = "Vigilante"
		verbose_name_plural= "Vigilantes"
	def __str__(self):
		return '(%s) %s' % (self.id, self.nombre_vigilante)

class grua(models.Model):
	nombre_grua = models.CharField(max_length=50, help_text='Nombre de la Compañia de Gruas')
	tipo_grua = (('O', 'OFICIAL'),
                    ('P', 'PARTICULAR'),
                    ('T', 'OTRO')
                )
	grua_tipo = models.CharField(max_length=1, choices=tipo_grua, default='C',help_text='Elije una opción')
	direccion_grua = models.CharField(max_length=100, help_text='Dirección de la compañia de Gruas')
	telefono_grua =  models.CharField(max_length=10, help_text='número telefonico')

	class Meta:
		ordering = ['nombre_grua']
		verbose_name = "Grua"
		verbose_name_plural= "Gruas"
	def __str__(self):
		return '(%s) %s' % (self.id,self.nombre_grua)

class deposito(models.Model):
	nombre_deposito = models.CharField(max_length=50, help_text='Nombre de Pila del deposito')
	direccion_deposito = models.CharField(max_length=120, help_text='Dirección del deposito')
	fecha_funcion = models.DateField(null=True, blank=True)
	fecha_cierre = models.DateField(null=True, blank=True)
	responsable = models.CharField(max_length=50, help_text='Nombre Completo empezando por Nombre, Apellido Paterno, Apellido Materno')
	telefono_resp = models.CharField(max_length=10, help_text='número telefonico')
	class Meta:
		ordering = ['nombre_deposito']
		verbose_name = "Deposito"
		verbose_name_plural= "Depositos"
	def __str__(self):
		return '(%s) %s' % (self.id, self.nombre_deposito)

class Oficio(models.Model):
	nombre_aut = models.ForeignKey('Autoridad', on_delete= models.SET_NULL, null=True)
	num_oficio = models.CharField(max_length=20, help_text= 'Ingrese el número de Oficio')
	fecha = models.DateField(null=True, blank=True)
	hora = models.TimeField(null=True, blank=True)
	tipo_expediente = (('N', 'NUAT'),
                    ('C', 'CDI'),
                    ('A', 'AP'),
                    ('O', 'OTRO')
                    )

	expediente = models.CharField(max_length=1, choices=tipo_expediente, default='C',help_text='Elije una opción')
	numero_exp = models.CharField(max_length=50, help_text= 'Ingrese el número de expediente')
	nombre_remite = models.ForeignKey('remite', on_delete= models.SET_NULL, null=True)
	nombre_vigilante = models.ForeignKey('vigilante', on_delete= models.SET_NULL, null=True)
	class Meta:
		ordering = ['num_oficio']
		verbose_name = "Oficio"
		verbose_name_plural= "Oficios"
	def __str__(self):
		return '(%s) %s' % (self.id, self.num_oficio)

class vehiculo(models.Model):
	Num_expediente = models.CharField(max_length=15, help_text='Formato = 170/R/2019')
	num_oficio = models.ForeignKey('Oficio', on_delete= models.SET_NULL, null=True)
	nombre_aut = models.ForeignKey('Autoridad', on_delete= models.SET_NULL, null=True)
	nombre_grua = models.ForeignKey('grua', on_delete= models.SET_NULL, null=True)
	nombre_deposito = models.ForeignKey('deposito', on_delete= models.SET_NULL, null=True)
	fecha_ingreso = models.DateField(null=True, blank=True)
	marca = models.CharField(max_length=15, help_text='Marca del vehículo')
	tipo = models.CharField(max_length=15, help_text='Tipo del vehículo')
	color = models.CharField(max_length=15, help_text='Color del vehículo')
	modelo = models.CharField(max_length=4, help_text='Modelo del vehículo')
	placa = models.CharField(max_length=10, help_text='Número de placa de circulación del vehículo')
	estado = models.CharField(max_length=15, help_text='Estado de las placas de circulación del vehículo')
	serie = models.CharField(max_length=17, help_text='Serie del vehículo')
	motor = models.CharField(max_length=20, help_text='Número del motor del vehículo')
	clase_auto =    (( 'A', 'AUTOMOVIL / CAMIONETA'),
					( 'B', 'CAMIONETA DE CARGA'),
					( 'C', 'AUTOBUS'),
					( 'D', 'CAMION DE 2 o 3 EJES'),
					( 'E', 'CAMION DE 4 o 5 EJES'),
					( 'F', 'CAMION DE 6,7,8, o 9 EJES'),
					( 'G', 'MOTOCICLETA')
					)
	tipo_auto = models.CharField(max_length=1, choices=clase_auto, default='A',help_text='Elije una opción')
	tipo_estatus = (( 'P', 'POR PAGAR'),
					( 'G', 'PAGADO'),
					( 'A', 'ABANDONADO'),
					( 'C', 'CHATARRIZACION')
					)
	estatus = 	models.CharField(max_length=1, choices=tipo_estatus, default='P',help_text='Elije una opción')
	sinofleje = (('S', 'SI'),
				  ('N', 'NO')	
				)
	fleje = 	models.CharField(max_length=1, choices=sinofleje, default='N',help_text='Elije una opción')
	folio_fleje = models.CharField(max_length=10, help_text='Folio del fleje',null=True, blank=True)
	tipo_motivo = (( 'R', 'ROBADO RECUPERADO'),
					( 'A', 'ASEGURADO'),
					( 'C', 'CATEO'),
					( 'O', 'OTRO')
					)
	motivo =  models.CharField(max_length=1, choices=tipo_motivo, default='R',help_text='Elije una opción')
	particular = (( 'P', 'PARTICULAR'),
					( 'E', 'EMPRESARIAL'),
					( 'O', 'OFICIAL')
				)
	procedencia = models.CharField(max_length=1, choices=particular, default='P',help_text='Elije una opción')
	edo_vehiculo = (( 'B', 'BUENO'),
					( 'R', 'REGULAR'),
					( 'M', 'MALO')
				)
	estado_veh = models.CharField(max_length=1, choices=edo_vehiculo, default='B',help_text='Elije una opción')
	llaves_vehiculo =(( 'S', 'SI'),
					  ( 'N', 'NO')
					 )
	llaves = models.CharField(max_length=1, choices=llaves_vehiculo, default='N',help_text='Elije una opción')
	func_vehiculo =(( 'S', 'SI'),
					  ( 'N', 'NO')
					 )
	funciona = models.CharField(max_length=1, choices=func_vehiculo, default='N',help_text='Elije una opción')
	sellado_vehiculo =(( 'S', 'SI'),
					  ( 'N', 'NO')
					 )
	sellos = models.CharField(max_length=1, choices=sellado_vehiculo, default='N',help_text='Elije una opción')
	valor_vehiculo =(( 'S', 'SI'),
					  ( 'N', 'NO')
					 )
	valores = models.CharField(max_length=1, choices=valor_vehiculo, default='N',help_text='Elije una opción')
	especifique= models.TextField(max_length=200,
                                     help_text='Aqui puede hacer descripción de los valores del autos',null = True, blank = True)
	observacion= models.TextField(max_length=200,
                                     help_text='Aqui puede hacer observaciones del vehiculo, entre otras',null = True, blank = True)
	Sasca =  models.CharField(max_length = 10, help_text = 'Ingrese el número de Sasca',blank= True,null=True)
	class Meta:
		ordering = ['Num_expediente']
		verbose_name = "Vehiculo"
		verbose_name_plural= "Vehiculos"
	def __str__(self):
		return '(%s) %s' % (self.id, self.Num_expediente)

class devolucion(models.Model):
	Num_expediente = models.ForeignKey('vehiculo', on_delete= models.SET_NULL, null=True)
	nombre_aut = models.ForeignKey('Autoridad', on_delete= models.SET_NULL, null=True)
	num_oficio = models.CharField(max_length=20, help_text= 'Ingrese el número de Oficio')
	fecha_oficio = models.DateField(null=True, blank=True)
	fecha_entrega = models.DateField(null=True, blank=True)
	hora_entrega = models.TimeField(null=True, blank=True) 
	entrega= models.CharField(max_length=50,help_text='Nombre completo del personal que entrega')	
	nombre_propietario = models.CharField(max_length=50, help_text='Nombre Completo empezando por Nombre, Apellido Paterno, Apellido Materno')
	tipo_iden = ( ('I', 'INE - IFE'),
				  ('C', 'CEDULA PROFESIONAL'),
				  ('P', 'PASAPORTE'),
				  ('L', 'LICENCIA DE CONDUCIR'),
				  ('CM', 'CARTILLA DEL SERVICIO MILITAR'),
				  ('O', 'OTRO')
				)
	identificacion = models.CharField(max_length=2, choices=tipo_iden, default='N',help_text='Elije una opción')
	numero_iden = models.CharField(max_length=20, help_text='Número de la identificación')
	telefono_usuario = models.CharField(max_length=10, help_text='Número telefonico')
	correo = models.EmailField()
	dias = models.CharField(max_length=5, help_text= 'Dias a resguardo')
	cobro = models.FloatField(default= 0.00)
	tipo_des = ( ('A', '0 %'),
				  ('B', '50 %'),
				  ('C', '100 %')
				)
	descuento = models.CharField(max_length=1, choices=tipo_des, default='A',help_text='Elije una opción')
	cobro_grua = models.FloatField(default= 0.00)
	class Meta:
		ordering = ['Num_expediente']
		verbose_name = 'Devolución'
		verbose_name_plural = 'Devoluciones'
	def __str__(self):
		return '%s' % (self.Num_expediente)
	




	
	

		
	