install:
    uv sync

VD-games:
    uv run VD-games

build:
    uv build

package-install:
    uv tool install --force dist/*.whl

lint:
    uv run ruff check VD_games