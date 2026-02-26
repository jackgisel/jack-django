# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Django 5.2 starter project using Python 3.12, PostgreSQL 16, Redis 7, and Celery. APIs are built with Django-Bolt (Rust-powered async JSON via msgspec). Frontend uses HTMX + Tailwind CSS (via django-tailwind-cli, no Node.js needed).

## Commands

All commands use `uv run` under the hood via the Makefile.

### Development
```bash
make install             # Install dependencies with UV
make docker-up           # Start Postgres + Redis containers
make migrate             # Run database migrations
make dev                 # Django dev server + Tailwind watcher (port 8000)
make bolt                # Django-Bolt API server in dev mode
make worker              # Run Celery worker
make admin               # Create superuser
```

### Code Quality
```bash
make lint                # Ruff linter (check only)
make format              # Ruff formatter (auto-fix)
make typecheck           # Ty type checker
make check               # lint + typecheck
```

### Docker
```bash
make docker-up           # Postgres + Redis only
make docker-all          # Full stack (web + worker + db + redis)
make docker-down         # Stop all services
```

## Architecture

- **`config/`** — Django project settings, URL routing, Celery config, and Django-Bolt API setup
- **`users/`** — Custom User model (extends `AbstractUser`), views, and API endpoints
- **`templates/`** — Django templates with `base.html` (HTMX + Tailwind), partials directory
- **`static/css/`** — Tailwind input/output CSS

### Key Patterns
- **Custom User model**: `users.User` (AUTH_USER_MODEL = "users.User"), db_table = "users"
- **Django-Bolt APIs**: Async endpoints using `msgspec.Struct` for serialization (see `config/api.py`, `users/api.py`)
- **Environment config**: All secrets via `.env` using `django-environ` (see `.env.example`)
- **Redis**: Used for both Django caching and Celery broker/result backend

### URL Structure
- `/admin/` — Django admin
- `/health/` — Health check (JSON)
- `/` — Home page
- `/users/` — Users app routes
- Django-Bolt API endpoints defined in `config/api.py` and `users/api.py`

## Code Style

- Ruff: line length 120, target Python 3.12, double quotes
- First-party imports: `config`, `users`
- Ruff rules: E, W, F, I, B, C4, UP, DJ, SIM
