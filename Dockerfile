FROM python:3.4

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python todo/manage.py migrate

CMD ["python","todo/manage.py","runserver","0.0.0.0:8000"]
