# FoxProject - ERP E-commerce with Django + Docker

This project is an ERP system for an e-commerce platform, built with **Django**, **Django REST Framework**, and professionally deployed using **Docker**.

## Requirements

* Docker
* Docker Compose
* Make (optional, for simplified commands)
* SSH key configured on GitHub

---

## Project Structure

```
FoxProject/
├── ecommerce_erp/               # Main Django project
├── products/                    # Example app
├── settings/                    # Professional settings (base, dev, prod)
├── scripts/                     # Helper scripts (entrypoint, wait_for_db)
├── .env.dev                     # Development environment variables
├── .env.db                      # Database environment variables
├── .env.dev.example             # Example for GitHub
├── .env.db.example              # Example for GitHub
├── Dockerfile                   # Web app Docker image
├── docker-compose.yml           # Web and DB services
├── Makefile                     # Handy commands (build, up, down...)
├── requirements.txt             # Python dependencies
└── README.md                    # Documentation
```

---

## Local Setup (first time)

1. **Clone the repository:**

```bash
git clone git@github.com:OswaldoZanca/FoxProject.git
cd FoxProject
```

2. **Copy the environment files:**

```bash
cp .env.dev.example .env.dev
cp .env.db.example .env.db
```

3. **Review and adjust the environment variables if needed**, especially:

* `SECRET_KEY`
* Ensure `POSTGRES_PASSWORD` and `DB_PASSWORD` match

4. **Start the project:**

```bash
make up
```

This will:

* Build the Docker image
* Initialize PostgreSQL with a persistent volume
* Apply migrations automatically
* Launch Django dev server at `http://localhost:8000`

5. **Create a superuser (for /admin access):**

```bash
docker compose exec web python manage.py createsuperuser
```

---

## Useful Makefile Commands

```bash
make up            # Build and start containers
make down          # Stop containers
make clean         # Remove containers and volumes (reset DB)
make migrate       # Run migrations manually
make shell         # Open a bash shell in the web container
```

---

## Resuming the Project (after rebooting your PC)

```bash
cd FoxProject
make up
```

> This reuses existing volumes and configurations without losing data.

---

## Deploying on Other PCs (Windows or Ubuntu)

1. Clone the repo
2. Copy `.env.dev` and `.env.db` using the `.example` files
3. Run `make up`

Done. No need to install PostgreSQL or configure anything manually.

---

## Pending / Future Improvements

* Add Nginx + Gunicorn for `prod` environment
* Setup HTTPS with Let's Encrypt
* Implement CI using GitHub Actions or Gitea
* Add automated testing with `pytest`
* Push images to a private registry (DockerHub, GitHub Container Registry)

---

Thanks for using this ERP! 🚀
