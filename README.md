# NFT Generator

![CI](https://github.com/maximunya/nft-generator/actions/workflows/ci.yml/badge.svg)

A Django REST Framework service for minting and querying ERC-721 NFTs on the Ethereum Sepolia
testnet via [web3.py](https://web3py.readthedocs.io/).

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Docker](#docker)
- [Testing, Linting, Type Checking](#testing-linting-type-checking)
- [API Endpoints](#api-endpoints)

## Features

- **Mint NFT** — create a new token by calling `mint` on an ERC-721 smart contract.
- **List tokens** — retrieve all tokens minted through this service, stored in the database.
- **Total supply** — read the current total supply directly from the blockchain.

## Tech Stack

- Python 3.12, Django 5, Django REST Framework
- [web3.py](https://web3py.readthedocs.io/) for blockchain interaction
- PostgreSQL (SQLite by default for local development)
- [uv](https://docs.astral.sh/uv/) for dependency management
- pytest, ruff, mypy, GitHub Actions CI
- Docker / Docker Compose
- Swagger / ReDoc API docs via drf-yasg

## Quick Start

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
git clone https://github.com/maximunya/nft-generator.git
cd nft-generator
uv sync
uv run manage.py migrate
uv run manage.py runserver
```

The API is now available at [http://localhost:8000/](http://localhost:8000/), backed by a local
SQLite database — no further configuration needed to browse the admin panel, Swagger docs, or the
token list endpoint. Minting tokens or reading total supply requires blockchain credentials (see
[Configuration](#configuration)).

Create an admin user with:

```bash
uv run manage.py createsuperuser
```

## Configuration

All configuration is read from environment variables (loaded from a `.env` file if present).

| Variable            | Required | Description                                              |
|---------------------|----------|------------------------------------------------------------|
| `SECRET_KEY`        | no       | Django secret key. Defaults to an insecure dev key.       |
| `DEBUG`              | no       | `True`/`False`. Defaults to `False`.                      |
| `DB_ENGINE`          | no       | Defaults to SQLite. Set to `django.db.backends.postgresql` to use Postgres. |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | when using Postgres | Postgres connection settings. |
| `DB_HOST_PORT`, `APP_PORT` | no (Docker only) | Host ports docker-compose exposes Postgres/the API on. Default `5432`/`8000`. |
| `INFURA_URL`         | for minting/total supply | RPC endpoint, e.g. an Infura Sepolia project URL. |
| `CONTRACT_ADDRESS`   | no       | ERC-721 contract address. Defaults to the project's demo Sepolia contract. |
| `CONTRACT_ABI`       | no       | JSON-encoded contract ABI. Defaults to [`tokens/contract_abi.json`](tokens/contract_abi.json); set this to use a different contract. |
| `PUBLIC_ADDRESS`     | for minting | Ethereum address used to sign mint transactions.       |
| `PRIVATE_KEY`        | for minting | Private key for `PUBLIC_ADDRESS`. Keep this secret.     |
| `CHAIN_ID`, `GAS_LIMIT` | no    | Defaults to Sepolia (`11155111`) and `300000` gas. Override for a different network. |

## Docker

```bash
cp .env.example .env
# fill in SECRET_KEY, INFURA_URL, PUBLIC_ADDRESS, PRIVATE_KEY in .env
docker compose up --build
```

This starts the Django service (built with `uv`, running as a non-root user) alongside a
PostgreSQL database, and applies migrations automatically on startup. The API is available at
[http://localhost:8000/](http://localhost:8000/). If ports 5432/8000 are already taken locally,
set `DB_HOST_PORT`/`APP_PORT` in `.env` to different values.

## Testing, Linting, Type Checking

```bash
uv run pytest          # test suite (pytest-django, SQLite in-memory)
uv run ruff check .    # lint
uv run ruff format .   # format
uv run mypy .          # static type checking
```

All three run in CI on every push and pull request (see `.github/workflows/ci.yml`).

## API Endpoints

### Create Token

- **Endpoint:** `POST /api/tokens/create/`
- **Body:** `media_url` (string), `owner` (Ethereum address)
- **Response:** the created Token object.

### List Tokens

- **Endpoint:** `GET /api/tokens/list/`
- **Response:** paginated list of Token objects.

### Total Supply

- **Endpoint:** `GET /api/tokens/total_supply/`
- **Response:** total token supply read from the blockchain.

### Additional Endpoints

| Endpoint     | Description                          |
|--------------|---------------------------------------|
| `/admin/`    | Django admin panel.                   |
| `/swagger/`  | Swagger UI API documentation.         |
| `/redoc/`    | ReDoc API documentation.              |
| `/api-auth/` | DRF browsable API authentication.     |
