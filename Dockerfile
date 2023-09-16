FROM openshift/python:3.6

RUN pip3 install flask 

COPY app.py /opt/

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080