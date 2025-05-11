# Makefile

PROJECT_NAME=ecommerce_erp
COMPOSE=docker compose
DJANGO_CONTAINER=web

up:
	$(COMPOSE) up --build

down:
	$(COMPOSE) down

restart:
	$(COMPOSE) down && $(COMPOSE) up --build

migrate:
	$(COMPOSE) exec $(DJANGO_CONTAINER) python manage.py migrate

makemigrations:
	$(COMPOSE) exec $(DJANGO_CONTAINER) python manage.py makemigrations

createsuperuser:
	$(COMPOSE) exec $(DJANGO_CONTAINER) python manage.py createsuperuser

shell:
	$(COMPOSE) exec $(DJANGO_CONTAINER) python manage.py shell

bash:
	$(COMPOSE) exec $(DJANGO_CONTAINER) bash

collectstatic:
	$(COMPOSE) exec $(DJANGO_CONTAINER) python manage.py collectstatic --noinput

logs:
	$(COMPOSE) logs -f

