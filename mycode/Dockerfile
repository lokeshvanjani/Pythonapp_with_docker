FROM python:3.7-buster

WORKDIR /mycode

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /mycode .

CMD["python","app.py"]