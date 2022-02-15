first commit para subir el proyecto ordenado y replicable
automatizacion QA de API con python y pytest

el proyecto tienen dentro un virtual environment dentro de otro.
people-api-master es un venv que contiene un webserver, base de datos y las APIs para testear
desempaquetar el zip
dentro de la carpeta desempaquetada people-api-master ejecutar:
para iniciar el venv
pipenv shell 
para instalar las dependencias
pipenv install
para crear la base de datos
python build_database.py
para inicar el server
python server.py
si se trabaja en windows hay que modificar la linea 15 de server.py para que quede así:
app.run(host='127.0.0.1', port=5000, debug=True)

con cualquier explorador ingresar a:
linux o mac: 0.0.0.0:5000
windows:127.0.0.1:5000
si te muestra un formulario para ingresar first name y last name, si te deja crear entradas y se muestran a continuacion... ya estamos listos.
