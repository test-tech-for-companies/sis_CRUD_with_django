# REST API Authenticación de usuarios

Este es un ejemplo pequeño que te permite interacturar con token de acceso para acceder a ciertos recursos de los usuarios

## Setup
* Obtenemos una copia del código

```bash
git clone https://github.com/test-tech-for-companies/sis_CRUD_with_django.git
cd sis_CRUD_with_django
```

* Creamos un ambiente virtual de python, instalamos dependencias,

```bash
python -m venv env
env\Scripts\activate
```

* Preparamos las variables de entorno en un nuevo archivo .env y cambiamos las siguientes variables que serán las credenciales de acceso a la base de datos MySQL

```bash
cp .env.example .env
```

Vamos a cambiar los valores para las siguientes:
```
MYSQL_DATABASE=your_db
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_HOST=your_ip
MYSQL_PORT=your_port
```

## Installation
* Luego instalamos dependencias 

```bash
(env) python -m pip install -r requirements.txt
```

Nota: asegurarse que en el prompt aparezca `(env)` nos indica que nuestro entorno virtual está activado

## Usage
* Ahora realizamos la generación de migraciones y luego las ejecutamos en nuestra base de datos

```bash
(env) python manage.py makemigrations
(env) python manage.py migrate
(env) python manage.py runserver
```

*  Asegurate de que en tu navegador esté corriendo

```bash
curl --write-out "%{http_code}\n" --silent --output /dev/null http://127.0.0.1:8000
```

* Como estamos en etapa de desarrollo te debería retornar codigo de estado 404, es la página de debugging que tiene activa la aplicación.


## Access to our application resources

### Signup endpoint

* Enpoint para registrar usuarios `/signup/`

* Preparamos un archivo .json con la información de nuestro usuario candito

    * Input:

        ```json
        {
            "name": "francisco",
            "password": "contraseña",
            "email": "fjgomezpe@misionTIC.com"
        }
        ```
* Hacemos test 

```bash
        curl http://127.0.0.1:8000/signup/ \
        -X POST \
        -H "Content-Type: application/json" \
        -d @user1.json \
        -vvv \
        ; echo "" | cat -e \
```

    * Output: Token de acceso, creado y almacenado en nuestra applicación

```json
    {
        "token":"169cbf18e79c24a94b203b358eea5c519d362427"
    }
```

    Dicho token te permitirá tener acceso los recursos dados en los endpoints:

    * /detail/<int:pk>/ [name='detail-user']
    * /change/<int:pk>/ [name='update-user']
    * /no-user/<int:pk>/ [name='delete-user']

### Login endpoint

* Enpoint para acceder a la aplicación `/login/`

* Preparamos un archivo .json con la información de nuestro usuario candito

    * Input:

        ```json
        {
            "password": "contraseña",
            "email": "fjgomezpe@misionTIC.com"
        }
        ```
* Hacemos test 

```bash
        curl http://127.0.0.1:8000/login/ \
        -X POST \
        -H "Content-Type: application/json" \
        -d @login1.json \
        -vvv \
        ; echo "" | cat -e \
```

    * Output: Token de acceso devuelto al usuario desde nuestra base de datos

```json
    {
        "token":"169cbf18e79c24a94b203b358eea5c519d362427"
    }
```

    Dicho token te permitirá tener acceso los recursos dados en los endpoints:

    * detail/<int:pk>/ [name='detail-user']
    * change/<int:pk>/ [name='update-user']
    * no-user/<int:pk>/ [name='delete-user']


### Detail user endpoint

* Enpoint para acceder a la aplicación `/detail/<int:pk>`
* Este enpoint requiere del token de acceso para ser consumido

* Preparamos un archivo .json con la información de nuestro usuario candito


    * Hacemos test 

```bash
        curl http://127.0.0.1:8000/detail/1/ \
        -X GET \
        -H "Authorization: Token 169cbf18e79c24a94b203b358eea5c519d362427" \
        -vvv \
        ; echo "" | cat -e \        
```

    * Output: Obtendremos los datos del usuario

```json
    {
        "id": 1,
        "name": "francisco", 
        "email":"fjgomezpe@misiontic.com"
    }
```



## Credits

Github: @juan-skill
