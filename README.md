# Django-to-do
A dead simple Django ToDo Web App

This is a sample project that a novice django developer can use to get started.

## Working

![Django to do](results/django-to-do.gif)

## Features

- Dead simple
- Easily add, delete
- Simple UI
- Blazing fast

## Setup

Requer **Python 3.10+** (o projeto foi migrado do Django 2.0 para o **Django 5.2 LTS**).

- Download the files from this repo
- Change the directory to the folder where you downloaded files
- Create a virtual environment and install the required packages:

    ```bash
    python -m venv .venv
    .venv\Scripts\activate        # Windows  (Linux/macOS: source .venv/bin/activate)
    pip install -r requirements.txt
    ```

- After successful installation execute the following commands:

    ```bash
    cd todo
    python manage.py migrate
    python manage.py runserver
    ```

- Run the automated tests:

    ```bash
    python manage.py test tasks
    ```

- Visit `127.0.0.1:8000` in your browser to enjoy the awesome app!

Built with ♥ by [`Omkar Pathak`](http://www.omkarpathak.in/)

# Donation

If you have found my softwares to be of any use to you, do consider helping me pay my internet bills. This would encourage me to create many such softwares :)

| PayPal | <a href="https://paypal.me/omkarpathak27" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg" alt="Donate via PayPal!" title="Donate via PayPal!" /></a> |
|:-------------------------------------------:|:-------------------------------------------------------------:|
| ₹ (INR)  | <a href="https://www.instamojo.com/@omkarpathak/" target="_blank"><img src="https://www.soldermall.com/images/pic-online-payment.jpg" alt="Donate via Instamojo" title="Donate via instamojo" /></a> |
