# base image
FROM python:3.6
#Permisos
USER root
# set working directory
RUN mkdir /app
WORKDIR /app
# install dependencies
COPY /requirements.txt /app/
RUN pip install -r requirements.txt
#Copiamos archivos
COPY . /app
# start app
CMD ["python", "app.py"]

# Contruccion
# docker build -t pokemon-app .
# Ejecucion
# docker run --rm -it -p 8082:8082 pokemon-app


# Fuente: https://aulasoftwarelibre.github.io/taller-de-docker/dockerfile/
# Construir
# docker build -t sedesa-back .
# Ejecutar
# docker run --rm -it -p 8082:8082 sedesa-back

# Nuevos requerimientos:
# pip freeze > requirements.txt
# o agregar a mano, revisando con pip list