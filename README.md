# cs50w-project4

Mi proyecto final:
    Mapa interactivo de Nicaragua. Hecho con python-Flask, html, scss y sqlalchemy
    Este proyecto pretende crear una página Web que sea utilizada para mostrar información sobre los distintos departamentos del país 
    en los apartados de Geografía, Historia y Cultura.

    Como función especial se pretende crear un apartado de preguntados el cual haría una serie de preguntas al usuario donde dará puntos 
    por cada pregunta correcta(En proceso):

   Tecnologías: 
        python: Flask
        html: html 5
        scss: Para dar estilos al proyecto
        JavaScript: Se espera agregar estilos extras con JavaScript
        sqlalchemy: para guardar la información sobre los departamentos y sobre el usuario

        Gimp2: puse esta tecnología porque creí que guardaría las imagenes del proyecto en el proyecto y en el caso de modificar alguna imagen utilizaría este programa

    Archivos: 
        templates: Contiene todos los html que usa la página web 
        Cultura: Contiene todos los archivos con la distinta información de los departamentos sobre su cultura 
        dirección imagenes: contiene las direcciones de las imagenes a mostrar al usuario 
        Geografía:  Contiene todos los archivos con la distinta información de los departamentos sobre su Geografía 
        Historia: Contiene todos los archivos con la distinta información de los departamentos sobre su Historia 
        Preguntas: contiene las preguntas y las respuestas del apartado de preguntados
        Static: contiene los estilos, imagenes y .js 
            image: contiene las imagenes utililzadas en el proyecto 
            Style: contiene el archivo. scss que da estilos al proyecto
            scripts.js:  espero agregar más estilos con el
        .env: Contiene las variables de entorno 
        application.py: la aplicación de flask
        archivos.py: el script para subir la información de cultura, geografía, historia y preguntas a la base de datos 
        credenciales: contiene las credenciales de la base de datos 
        funciones: contiene las funciones extras del programa como lo es limpiarlinea que limpia el formato de los html que muestran la información 
        requirements: contiene los requerimientos para correr el proyecto


Observaciones del jurado : 
    background color 
        Cambie el color de fondo a  antiquewhite

    Acceso al resto de información del mismo departamento
        Se hicieron 2 botones de acceso para cambiar de apartado desde el departamento en que se encuentra el usuario 

    Footer agregar información de contacto
        Agregue en contacto de instagram, facebook y mi perfil de GitHub

    Terminar preguntados
        
Las observaciones hechas por el jurado fueron implementadas en el proyecto:
https://github.com/BlueAACJ/Mapa-Interactivo-Web
