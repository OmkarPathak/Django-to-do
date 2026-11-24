# Django-to-do

[![CI](https://github.com/jvpaim/Django-to-do/actions/workflows/ci.yml/badge.svg)](https://github.com/jvpaim/Django-to-do/actions/workflows/ci.yml)
[![Release](https://github.com/jvpaim/Django-to-do/actions/workflows/release.yml/badge.svg)](https://github.com/jvpaim/Django-to-do/actions/workflows/release.yml)
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

- Create the local environment file and generate a new secret key:

    ```powershell
    Copy-Item .env.example .env
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```

    Replace `DJANGO_SECRET_KEY` in `.env` with the generated value. Keep
    `DJANGO_DEBUG=True` only for local development. The `.env` file must never
    be committed.

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

## CI e releases

O projeto usa GitHub Actions (`.github/workflows/`):

| Workflow | Quando roda | O que faz |
|---|---|---|
| `ci.yml` | push na `master`, PRs | lint (ruff), `manage.py check`, verificação de migrações pendentes, testes em Python 3.10–3.13 com cobertura (mínimo 80%), auditoria de vulnerabilidades (`pip-audit`) |
| `pr-title.yml` | PRs | exige título no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/) |
| `release.yml` | push na `master` | [release-please](https://github.com/googleapis/release-please): mantém um PR de release com `CHANGELOG.md` e versão nova; ao fazer merge dele cria a tag `vX.Y.Z`, o GitHub Release e anexa o código empacotado |

O Dependabot (`.github/dependabot.yml`) abre PRs de atualização de dependências e das actions.

### Versionamento

As versões seguem [SemVer](https://semver.org/lang/pt-BR/) e são calculadas a partir das mensagens de commit:

- `fix: ...` → patch (1.0.0 → 1.0.1)
- `feat: ...` → minor (1.0.0 → 1.1.0)
- `feat!: ...` ou rodapé `BREAKING CHANGE:` → major (1.0.0 → 2.0.0)
- `docs:`, `test:`, `ci:`, `chore:`, `refactor:` → não geram release sozinhos

A versão atual fica em `pyproject.toml` e `.release-please-manifest.json`; não edite à mão.

### Rodando as verificações localmente

```bash
pip install -r requirements-dev.txt
ruff check .
cd todo
python manage.py makemigrations --check --dry-run
coverage run --rcfile=../pyproject.toml manage.py test
coverage report --rcfile=../pyproject.toml
```

Built with ♥ by [`Omkar Pathak`](http://www.omkarpathak.in/)

# Donation

If you have found my softwares to be of any use to you, do consider helping me pay my internet bills. This would encourage me to create many such softwares :)

| PayPal | <a href="https://paypal.me/omkarpathak27" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg" alt="Donate via PayPal!" title="Donate via PayPal!" /></a> |
|:-------------------------------------------:|:-------------------------------------------------------------:|
| ₹ (INR)  | <a href="https://www.instamojo.com/@omkarpathak/" target="_blank"><img src="https://www.soldermall.com/images/pic-online-payment.jpg" alt="Donate via Instamojo" title="Donate via instamojo" /></a> |
