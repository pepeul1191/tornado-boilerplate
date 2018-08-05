## Python3 Tornado Boilerplate

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate

Arrancar servidor Torando

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

Migraciones con DBMATE:

    $ dbmate -d "db/migrations" -e "DATABASE_URL" new <<nombre_de_migracion>>
    $ dbmate -d "db/migrations" up

### Fuentes:

+ http://www.tornadoweb.org/en/stable/
+ https://github.com/pepeul1191/tornado-animalitos
+ https://simplapi.wordpress.com/2014/03/26/python-tornado-and-decorator/
+ https://stackoverflow.com/questions/47010763/tornado-asynchronous-actions-in-custom-decorator

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
