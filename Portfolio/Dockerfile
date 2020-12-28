FROM python:3.9

EXPOSE 8000

ADD . /Portfolio

WORKDIR /Portfolio

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
