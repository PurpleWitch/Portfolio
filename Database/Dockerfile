FROM python:3.9

EXPOSE 8000

ADD . /Database

WORKDIR /Database

RUN pip install -r requirements.txt

CMD ["python","app.py"]
