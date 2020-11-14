FROM python:3.8 

COPY . /

RUN pip install -r requirements.txt

CMD gunicorn -w 4 --bind 0.0.0.0:8000 app.app:app
