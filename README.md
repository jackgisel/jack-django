# Jack's Django Starter

Production-ready Django starter for SaaS, personal apps, and scalable software.

## Stack

- **Django 5.2** - Web framework
- **Postgres** - Database
- **Redis** - Cache + Celery broker
- **Celery** - Background tasks
- **Tailwind CSS v4** - Styling (via django-tailwind-cli, no Node.js)
- **HTMX** - Dynamic frontend without JS
- **Django-Bolt** - High-performance Rust-powered JSON APIs
- **UV** - Fast Python package manager
- **Ruff** - Linter + formatter
- **Ty** - Type checker
- **Docker** - Local dev + production
- **Railway** - Deployment

## Quick Start

```bash
# Install dependencies
uv sync

# Start Postgres + Redis
make docker-up

# Copy env and run migrations
cp .env.example .env
make migrate

# Create admin user
make admin

# Run dev server (Django + Tailwind watcher)
make dev
```

Visit http://localhost:8000

## Commands

| Command | Description |
|---------|-------------|
| `make dev` | Django dev server + Tailwind watcher |
| `make bolt` | Django-Bolt API server (dev mode) |
| `make migrate` | Run database migrations |
| `make makemigrations` | Create new migrations |
| `make admin` | Create a superuser |
| `make worker` | Run Celery worker |
| `make lint` | Run Ruff linter |
| `make format` | Run Ruff formatter |
| `make typecheck` | Run ty type checker |
| `make check` | Run all checks (lint + typecheck) |
| `make docker-up` | Start Postgres + Redis |
| `make docker-down` | Stop Docker services |
| `make docker-all` | Start everything in Docker |

## Project Structure

```
config/          Django project config (settings, urls, celery, api)
users/           Custom User model + API endpoints
templates/       Jinja/Django templates (base.html, partials/)
static/css/      Tailwind CSS source
```
