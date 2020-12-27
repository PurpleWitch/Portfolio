FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app/api
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python manage.py runserver
COPY . ./
EXPOSE 8000