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

    Consultas MongoDB:

    + SELECT tipo, nombre FROM ubicaciones WHERE pais_id = {{pais_id}}

        db.ubicaciones.find(
          {
            pais_id: ObjectId("5b907d815139f844031cc5a1")
          },
          {
            tipo: 1,
            nombre:1
          }
        )

+ Consultar recursivas a árbol similar a:

  ```
  SELECT * FROM vw_distrito_provincia_departamento WHERE nombre LIKE 'La%' LIMIT 0,10;
  ```

  ```
  db.ubicaciones.aggregate([
    {
      $match:{
        tipo: "distrito"
      }
    },
    {
      $lookup:{
        from: "ubicaciones",
        localField: "provincia_id",
        foreignField: "_id",
        as: "provincia"
      }
    },
    {
      $unwind: {
        path: "$provincia",
        preserveNullAndEmptyArrays: true
      }
    },
    {
      $lookup: {
        from: "ubicaciones",
        localField: "provincia.departamento_id",
        foreignField: "_id",
        as: "departamento",
      }
    },
    {
      $unwind: {
        path: "$departamento",
        preserveNullAndEmptyArrays: true
      }
    },
    {
      $match:{
        "departamento.pais_id": ObjectId("5b90a5b1ef627560f1251e4d"),
        "nombre": /^La/
      }
    },
    { $project: {
        "_id": "$_id",
        "nombre": {
          $concat: [
            "$nombre",
            ", ",
            "$provincia.nombre",
            ", ",
            "$departamento.nombre"
          ]
        },
      }
    },
    {
      $limit: 10
    },
  ])
  ```

Almacenar función

~~~
db.system.js.save(
{
  _id: "buscarDistrito",
  value: function(pais_id, nombre){
    var docs = db.ubicaciones.aggregate([
      {
        $match:{
          tipo: "distrito"
        }
      },
      {
        $lookup:{
          from: "ubicaciones",
          localField: "provincia_id",
          foreignField: "_id",
          as: "provincia"
        }
      },
      {
        $unwind: {
          path: "$provincia",
          preserveNullAndEmptyArrays: true
        }
      },
      {
        $lookup: {
          from: "ubicaciones",
          localField: "provincia.departamento_id",
          foreignField: "_id",
          as: "departamento",
        }
      },
      {
        $unwind: {
          path: "$departamento",
          preserveNullAndEmptyArrays: true
        }
      },
      {
        $match:{
          "departamento.pais_id": ObjectId(pais_id),
          "nombre": nombre
        }
      },
      { $project: {
          "_id": "$_id",
          "nombre": {
            $concat: [
              "$nombre",
              ", ",
              "$provincia.nombre",
              ", ",
              "$departamento.nombre"
            ]
          },
        }
      },
      {
        $limit: 10
      },
    ])
    return docs._batch;
  }
});
~~~

Llamar funcion

~~~
db.eval('buscarDistrito("5b90a5b1ef627560f1251e4d","La Victoria")');
~~~

### Migraciones SQL

Migraciones con DBMATE - ubicaciones:

    $ dbmate -d "db/migrations" -e "DATABASE_UBICACIONES" new <<nombre_de_migracion>>
    $ dbmate -d "db/migrations" -e "DATABASE_UBICACIONES" up

### Comandos backup de MongoDB

    $ mongodump --db ubicaciones --host localhost --port 27017 --out db

### Comandos restore de MongoDB

    $ mongorestore --db ubicaciones --host localhost --port 27017 db/ubicaciones


### Fuentes:

+ http://www.tornadoweb.org/en/stable/
+ https://github.com/pepeul1191/tornado-animalitos
+ https://simplapi.wordpress.com/2014/03/26/python-tornado-and-decorator/
+ https://stackoverflow.com/questions/47010763/tornado-asynchronous-actions-in-custom-decorator
+ http://www.tornadoweb.org/en/stable/guide/templates.html?highlight=ui_methods#template-syntax
+ https://stackoverflow.com/questions/12993835/passing-a-custom-python-function-into-a-tornado-template
+ https://stackoverflow.com/questions/10726486/tornado-url-query-parameters

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
