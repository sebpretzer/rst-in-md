install:
	uv sync --all-extras
	uv run pre-commit install

lint:
	uv run pre-commit run --all-files

test:
	uv run pytest

build:
	uv run hatch build -c

mkdocs-dev:
	uv run mkdocs serve

mkdocs-check:
	uv run mkdocs build --clean --strict

mkdocs-publish:
	uv run mkdocs gh-deploy --clean --force

uv-install:
	curl -LsSf https://astral.sh/uv/install.sh | sh
