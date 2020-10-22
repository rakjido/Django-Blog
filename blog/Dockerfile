FROM python:3.7.7

COPY . /app

WORKDIR /app 

RUN pip install -r requirement.txt

CMD ["uwsgi", "uwsgi.ini"]