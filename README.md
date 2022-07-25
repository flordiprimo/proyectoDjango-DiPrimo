# Proyecto Coder

**Alumna:** Maria Florencia Di Primo
*(Pablo Zorrilla informó que no iba a poder participar de la entrega y nunca recibí respuesta o contacto alguno de Marcos Perafan, con lo cual continué haciendo la entrega sola, al igual que en la preentrega).*

## Pasos para abrir el proyecto desde el localhost
1. Descargar el repositorio y abrir la carpeta con Visual Studio Code
2. En la terminal, posicionarse en la carpeta del proyecto y utilizar los siguientes comandos: `python manage.py runserver`
3. Navegar hacia **http://localhost:8000/**

## Abrir el proyecto en Heroku
Se incluye una versión web del proyecto en la siguiente url: **https://young-island-96322.herokuapp.com/**
*Nota: Los estáticos en Heroku se muestran sin problema, no así los Media Files como Avatars e imágenes de producto porque lamentablemente Heroku no las muestra correctamente y Whitenoise no soporta media files así que no pude resolverlo de esa manera. Investigando, requería de otros add-ons o almacenamiento en otros servidores, cosa que por cuestiones de tiempo no pude implementar.*

## Página de inicio y menú de navegación
En la página de inicio se puede acceder a las distintas categorías (Remeras, Pantalones y Camisas) desde la barra de navegación o desde el botón de cada una en el carrousel sin necesidad de estar logueado como usuario. 
1. Si el usuario se loguea como administrador *(user: admin/ pass: admin)* el menú muestra la posibilidad de Editar Productos, lo que permite agregar nuevos productos en cada categoría, editar información e imagen de producto o borrarlos.
2. Si el usuario se loguea como un usuario que no es staff *(usuario creado desde la interfaz registrarse)* no tendrá la posibilidad de editar productos, sólo podrá visualizar/editar su perfil y cerrar sesión.

## Modelos y rutas de navegación
Cada categoría de producto tiene una página donde se visualizan todos los productos de ese modelo/clase. 
> Por ejemplo, la clase Remeras tiene una vista en http://localhost:8000/tienda/remeras donde se pueden visualizar todos los productos

En cada vista, se puede:
 - Ver todos los productos de la categoría con su imagen,
   características principales y posibilidad de acceder al detalle del
   producto
 - Acceder al buscador, que busca productos por modelo y
   devuelve resultados

## Dependencias

Las dependencias utilizadas fueron las siguientes

 - Django (4.0.5) 
 - Bootstrap (5.1.3) & Bootstrap icons (1.9.1)
 - Pillow (9.2.0)
 - Whitenoise (6.2.0)
 - Gunicorn (20.1.0)
 - Psycopg2-binary (2.9.3)
 - dj-database-url (0.5.0)

 ## Unit tests

Los casos de prueba se encuentran debidamente documentados en el archivo **Unit test.xlsx**