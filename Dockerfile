# Base Image
FROM python:3.7

# Working Directory
WORKDIR /app

# Code
COPY . .

# Libraries
RUN  pip install -r requirements.txt

# Migrations
RUN python todo/manage.py migrate

# RUN APP
CMD ["python","todo/manage.py","runserver","0.0.0.0:8000"]
