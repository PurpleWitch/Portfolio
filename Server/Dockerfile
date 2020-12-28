FROM python:3.9

EXPOSE 9000

ADD . /Server

WORKDIR /Server

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
