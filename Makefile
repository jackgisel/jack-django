.PHONY: help install dev bolt migrate makemigrations admin worker lint format typecheck check docker-up docker-down docker-all

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install all dependencies
	uv sync

dev: ## Run Django dev server with Tailwind watcher
	uv run python manage.py tailwind runserver

bolt: ## Run Django-Bolt API server (dev mode)
	uv run python manage.py runbolt --dev

migrate: ## Run database migrations
	uv run python manage.py migrate

makemigrations: ## Create new migrations
	uv run python manage.py makemigrations

admin: ## Create a superuser
	uv run python manage.py createsuperuser

worker: ## Run Celery worker
	uv run celery -A config worker --loglevel=info

lint: ## Run Ruff linter
	uv run ruff check .

format: ## Run Ruff formatter
	uv run ruff format .

typecheck: ## Run ty type checker
	uv run ty check .

check: lint typecheck ## Run all checks (lint + typecheck)

docker-up: ## Start Postgres + Redis only
	docker compose up -d db redis

docker-down: ## Stop all Docker services
	docker compose down

docker-all: ## Start all Docker services including web and worker
	docker compose up --build
