# DJANGO HOTEL API REST
# Requerimientos
Utilizando Django REST Framework, se desarrollará los endpoints para el sistema de reservas de habitación de un hotel.

CONDICIONES:
- Las reservas pueden tener 3 estados: Pendiente, Pagado y Eliminado.
- Los datos a almacenar para la reserva son: los detalles del cuarto reservado, los días de estadía, los datos de facturación e identificación del cliente, el monto pagado y el método de pago.
- Proponer los endpoints a crearse para tratar de cubrir el flujo normal de operación de reserva y explicar por qué.

# Análisis
De acuerdo al requerimiento se plantea un sistema transaccional, por esta razón se eligio  una base de datos relacional (PostgreSQL o cualquier otro) en este caso.
Al elegir una relacional debemos empezar por el modelo ver que responda a los requerimientos, para ellos definimos las siguientes tablas y relaciones:


![Model ER Django Hotel API](https://i.ibb.co/BfqLkdv/idiagramaer.png)
#### room_type 

#### room 
Son los cuartos en si y pueden estar codificados ejm. PB2, Planta Baja habitación 2.
Es posible que el API se use en web o moviles asi que colocamos la foto de la habitacion.
si la habitación esta disponible (is)_active=true) Y el tipo de cuarto de acuerdo a room_type (ejm. Habitacion simple, habitacion doble, habitacion matrimonial, etc.)
#### user
esta entidad es la que viene con django.contrib.auth, y esta todo el sistema de autenticacion. Para fines prácticos de este ejemplo usaremos esta tabla para registrar a los clientes (no es recomendable ya que tiene muchos campos que no siempre usaran los usuarios pero vale para el ejemplo).
colocamos varios campos como la photo(en caso que tenga un perfil el usuario), el telefono, ciudad,etc. y  también usamos esta tabla para el registro del NIT y el nombre a la que saldra la factura.
la propiedad is_recruter, usaremos para el sistema de permisos para diferenciar si este usuario es el administrador del hotel o no (en todo caso cliente)
#### booking 
Es ya la parte central del proyecto, 
- bookingDate, fecha que se realiza la reserva
- arrivalDate, cuando llegara al hotel (fecha que tomara el cuarto)
- day_of_stay, cuanto tiempo se va quedar tentativamente el cliente
- room y user, el cuarto que selecciona y vinculamos al cliente que esta haciendo la reserva
#### bill
Aqui ya se efectiviza el pago en si, se separo en otra tabla porque los pagos pueden en varias partes Ejm. 50% al ingresar y el otro 50% al salir, si el cliente decide quedarse unos dias mas etc. por eso se definio un historico para sacar un estado de cuenta del cliente.
- date, la fecha que se realizo el pago
- amount, el monto cancelado a ese momento
- booking, la reserva a la cual esta realizando el pago (puede tener varios cuartos reservados asi sabemos de cual esta pagando)
- bill_type, el motodo de pago ejm. efectivo o tarjeta. (no pusimos los datos de la tarjeta u otros porque seria extender el sistema pero sirve el modelo como una base) :)

# Despliegue
Para este proyecto usaremos Django con python 3 y usaremos un poco de docker y dockercompose para desplegarlo fácilmente.
Dockerfile

```docker
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```
el dockercompose.yml, para desplegar dos contenedores el web y la db
```docker
version: '3'
services:
db:
	image: postgres
	env_file:
		- ./.envs/.postgres
	volumes:
		- pgdata:/var/lib/postgresql/data
ports:
	- "5432:5432"
web:
	build: .
	command: python manage.py runserver 0.0.0.0:8000
	env_file:
		- ./.envs/.django
		- ./.envs/.postgres
	volumes:
		- .:/code
	ports:
		- "8000:8000"
	depends_on:
		- db
volumes:
	pgdata:
```
# Desarrollo
Con las herramientas elegidas, usaremos **DRF**, vamos a realizar un proyecto que será un  **CRUD** de varias tablase y nos facilitara hacerlo rapido.
En el que un usuario podrá registrarse como admin  o cliente para aparecer en las búsquedas. Ambos podrán autenticarse y el usuario admin podrá añadir información acerca de su cuartos, metodos de pagos, etc. El cliente solo podra hacer la reserva.
### Estructura
Todos los modulos estaran en la carpeta src
```bash
.
├── ...
├── src                    # carpeta con los modulos en el py
│   ├── bills              # modulo de pagos
│   ├── booking            # modulo de reservas
│   ├── rooms              # modulo de cuartos
│   ├── users              # modulo de users
│   └── ...                 # etc.
└── ...
```
### USERS
Ahora vamos a usar el modelo para usuarios, utilizaremos el modelo ya existente en Django para usuarios y añadiremos una fecha de modificación, la foto del usuario, teléfono, ciudad, país y los datos para la facturación. También modificaremos la configuración por defecto para que el login sea mediante el password en vez de por username.
Para no juntar el codigo todo en unos cuantos archivos vamos crear diferentes proyectos este sera el de Users y tendra sus propios modelos, views y serializares. esto para separa un poco la logica de negocio y sea un poco mas mantenible.


Para esta parte Usaremos TDD, Test-driven development en terminos sencillo primero hacer la prueba unitaria y después el código. Con esta práctica se consigue entre otras cosas: un código más robusto, más seguro, más mantenible.
las pruebas unitarias estan dentro del la carpeta users y tests.py
Tenemos algunos metodos que explicaremos
- setUp, este metodo hacemos una prueba para la configuracion de nuestro usuario
- test_signup_user, Aqui es donde probamos el registro de un usuario (puede ser un cliente) y simulamos incluso como envia una foto.
- test_login_user, a este usuario registrado le hacemos un login o un inicio de session
- test_fail_login_user, verificamos que si ponemos mal algun dato como correo o contraseña, el sistema te rechaza y no te entrega el token respectivo, por tanto ya no podras hacer ninguna actividad en el sistema.

```python
class  UserTestCase(TestCase):
	def  setUp(self):
		user = User(
			email='testing_login@hotel.bo',
			first_name='Testing',
			last_name='Testing',
			username='testing_login')
		user.set_password('admin123')
		user.save()
	def  test_signup_user(self):
		"""Verificamos si podemos crear un user"""
		image = Image.new('RGB', (100, 100))
		tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
		image.save(tmp_file)
		tmp_file.seek(0)

		client = APIClient()
		response = client.post(
		'/users/signup/',
		{
		'email': 'testing@hotel.bo',
		'password': 'rc{4@qHjR>!b`yAV',
		'password_confirmation': 'rc{4@qHjR>!b`yAV',
		'first_name': 'Testing',
		'last_name': 'Testing',
		'phone': '59170654074',
		'city': 'La Paz',
		'country': 'Bolivia',
		'photo': tmp_file,
		'extract': 'I am a testing',
		'invoice_nit': '4900112014',
		'invoice_name': 'invoice name',
		'username': 'testing1'
		},
		format='multipart'
	)
	self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	self.assertEqual(json.loads(response.content), 	{"username":"testing1","first_name":"Testing","last_name":"Testing","email":"testing@hotel.bo"})
 
	def  test_login_user(self):
		"""Verificamos si podemos hacer login con el user"""
		client = APIClient()
		response = client.post(
			'/users/login/', {
			'email': 'testing_login@hotel.bo',
			'password': 'admin123',
			},
			format='json'
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		result = json.loads(response.content)
		self.assertIn('access_token', result)

	def  test_fail_login_user(self):
		"""Verificamos si nos devuelve error con un password incorrecto y no devuelve el token"""
		client = APIClient()
		response = client.post(
		'/users/login/', {
		'email': 'testing_login@hotel.bo',
		'password': 'admin1234',
		},
		format='json'
		)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		result = json.loads(response.content)
		self.assertNotIn('access_token', result)
```
Hacemos correr nuestra bateria de pruebas  y vemos que no funcionara nada. Asi empezamos el codigo para responder a esos tests 
La idea general es usar DRF como lo explican en : https://www.bezkoder.com/django-rest-api/ y hacer una aplicacion rapida de reservas de hoteles.
![enter image description here](https://www.bezkoder.com/wp-content/uploads/2020/04/django-rest-api-tutorial-example-architecture.png)
Vendra la peticion, ira nuestro archivo urls.py -> lo redireccionara al controlador y este enviara al serializer o models de acuerdo a lo que necesite.
Aqui ya se puede ver el código desarrollado en la carpeta users, posteriormente luego de varias pruebas podemos realizar nuestra bateria de pruebas.
```bash
$ python manage.py test --debug-mode -d --traceback users
```
y vemos que sale el OK en la bateria de pruebas.
```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
----------------------------------------------------------------------
Ran 3 tests in 0.855s

OK
Destroying test database for alias 'default'...
```
### booking y bills
De igual forma se realiza los demas proyectos, se dividio en : bill, booking,room y users.
Search, es crear un forma de realizar busquedas en todos los modelos para los buscadores y no hacer uno por uno. Sera explicado mas adelante.
En cada una de las carpetas por DRF, ya tenemos el crud de forma casi automatica, asi que no valdria la pena explicar lo que esta en : https://www.django-rest-framework.org/

## TESTING
```bash
.
├── ...
├── tests                    # Test files (alternatively `spec` or `tests`)
│   ├── factory              # modela la generacion de datos para las pruebas
│   └── hotel                # Unit tests para cada modulo
└── ...
```

```python
$ python manage.py test -v 2
Creating test database for alias 'default' ('test_hotel')...
Operations to perform:
  Synchronize unmigrated apps: base, ckeditor, django_seed, drf_yasg, messages, rest_framework, shortuuidfield, simple_history, staticfiles
  Apply all migrations: admin, auth, bills, booking, contenttypes, rooms, sessions, users
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying users.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying rooms.0001_initial... OK
  Applying rooms.0002_historicalroom_history_user... OK
  Applying rooms.0003_auto_20220401_2133... OK
  Applying rooms.0004_auto_20220401_2139... OK
  Applying rooms.0005_auto_20220401_2159... OK
  Applying rooms.0006_auto_20220401_2202... OK
  Applying rooms.0007_auto_20220401_2222... OK
  Applying rooms.0008_alter_room_type... OK
  Applying booking.0001_initial... OK
  Applying booking.0002_auto_20220403_1716... OK
  Applying booking.0003_auto_20220403_1723... OK
  Applying bills.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying users.0002_alter_user_id... OK
System check identified no issues (0 silenced).
test_room_can_be_unavailable_after_reservation (tests.hotel.bill.test_bill.CreateBillTest)
test para registro de un pago dado una reserva ... ok
test_room_can_be_unavailable_after_reservation (tests.hotel.booking.test_booking.CreateBookingTest)
test para registro de una reserva ... ok
test_room1_can_record_room (tests.hotel.rooms.test_rooms.CreateRoomsTest)
Puede registrar un cuarto ... ok
test_room2_can_not_record_with_no_field_type (tests.hotel.rooms.test_rooms.CreateRoomsTest)
No Puede registrar un cuarto sin tipo de cuarto ... ok
test_room3_can_view_a_room (tests.hotel.rooms.test_rooms.CreateRoomsTest)
Puede ver un cuarto en particular en la url : /api/rooms/1 ... ok
test_room4_can_view_all_rooms (tests.hotel.rooms.test_rooms.CreateRoomsTest)
Puede listar todos los cuartos ... ok
test_signup_user (tests.hotel.users.test_users.UserTestCase)
Verificamos si podemos crear un user ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.897s

OK
Destroying test database for alias 'default' ('test_hotel')...
```
## FUNCIONALIDAD DE LOS APIS CON POSTMAN
para verificar nuestros APIS tambien podemos usar POSTMAN y simulemos un pequeño flujo como el siguiente :

1. Registro el cliente : POST:/users/signup/
	- tabla : users
	![enter image description here](https://i.ibb.co/ZWB9dvn/ipost0.png)
2. Login del cliente.
Una vez registrado el cliente,  iniciamos su login y este nos devuelve el token
![enter image description here](https://i.ibb.co/jJP3vp8/ipost1.png)
A partir de ahora es necesario configurar nuestro postman, para guardar ese token y utilizar ya que nos permitirá sino realizamos esta tarea.
![enter image description here](https://i.ibb.co/ZWFW0n6/ipost2.png)

3. Registrar el Cuarto
POST: /rooms/
Ejm. 
{
    "type": "Simple",
    "code": "PB1",
    "description": "Habitacion PB-1",
    "price_day": 100,
    "discount_rate": 10,
    "available": true
}
4. Realizar la Reserva  :  
POST:/booking
{
    "user": "2",
    "room": "2",
    "bookingDate": "2022-04-10",
    "arrivalDate": "2022-04-10",
    "day_of_stay": 2,
    "state": "Pendiente"
}
	- elige el room de acuerdo al room_type
	- se set el estado
	- se registra : bookingDate,arrivalDate,ArrivalDate,dias_estadia
	- validar que ese cuarto no este reservado en ese dia.

5. Se procede a realizar el pago	
POST:/bills/
{
    "debit": 100,
    "credit": 0,
    "booking": 1,
    "bill_type": "Efectivo",
    "date": "2022-04-10 09:00"
}
- bill es otra tabla porque acepta pagos parciales y se puede ir sumando para saber el saldo.

6. Ver el cliente puede ver su estado de cuenta y los pagos que realizo: GET:/bills/bill_payment_account?user=2&room=1
ahi podemos ver que realizo dos pagos, en determinadas fechas, lo cual en un reporte se puede sacar el total y esteblecer la deuda(si tuviera)


## DOCUMENTACION DEL API
- Para enteder un poco mas de los APIS que realizan los calculos imporantes se puede consultar a : https://documenter.getpostman.com/view/5404065/UVypzxcs

## RECOMENDACIONES
- Es un proyecto sencillo usando django y DRF, sin embargo, para escalar se deberia usar una arquitectura mas robusta (ejm microservicios). en esta ultima permiten ejecutar funciones por separado y, si es que por algún motivo un servicio falla, el resto seguirá funcionando sin verse afectado por el que tiene problemas.
- Podriamos mejorar el codigo usando algo mas de Solid y restructurar las carpetas y incorporar inyeccion de dependencias entre otras cosas para que sea mas mantenible y escalable.
- Tambien existen muchas posibilidades de extender el modelo, por ejemplo. guardar las preferencias del cliente (sin un ciente paga con tarjeta es muy probable que la siguiente que vuelva usara el mismo medio,etc) y estas se pueden guardar en tablas de preferencias. Utilizar un modelo para usar pasarelas de pago, etc.
- Se deberia separar users de los clientes, para que el modelo no este sobrecargado y sea  mantenible de mejor forma. En tablas es preferible crecer de forma vertical que horizontal, este por temas de performance.
- Una parte de la lógica se realizo en las consultas (querys) a la base de datos, si bien funciona, para que sea mas escalable se puede realizar gran parte de la lgoica en el backend (django), con la finalidad que que cuando el sistema escale, no este muy cargada la bdd y usar la misma solo como un repositorio para persistir la data.
- De acuerdo a la cantidad de peticiones y despues de un test de estres. ver como usar las colas de las peticiones y procecesos paralelos.

