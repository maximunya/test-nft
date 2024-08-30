# NFT Backend Service

This project is a backend service built using Django and Django REST Framework (DRF) to interact with an ERC-721 NFT smart contract on the Ethereum blockchain (Sepolia Testnet). The service allows you to mint new NFTs and retrieve information about existing NFTs via a REST API.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Docker Setup](#docker-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Features

- **Mint NFT:** Create new NFTs by interacting with an ERC-721 smart contract.
- **Retrieve Token List:** Get a list of all minted tokens stored in the database.
- **Check Total Supply:** Retrieve the total supply of tokens from the blockchain.

## Technologies

- **Python 3.7+**
- **Django 4+**
- **Django REST Framework**
- **Web3.py**
- **PostgreSQL**
- **Docker**
- **Swagger** (drf-yasg)

## Installation

### Clone the Repository

```bash
git clone https://github.com/maximunya/test-nft.git
cd test-nft
```

## Configuration

1. Copy the `.env.docker.template` file and rename it to `.env.docker`:

    ```bash
    cp .env.docker.template .env.docker
    ```

2. Open the `.env.docker` file and fill in the following environment variables:

    ```env
    SECRET_KEY=Your Django secret key
    DEBUG=True
   
    DB_NAME=Your DB Name
    DB_USER=Your DB User
    DB_PASSWORD=Your DB Password
    DB_HOST=Your DB Host
    DB_PORT=Your DB Port

    INFURA_URL=https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID
    CONTRACT_ADDRESS=0x399c1448e0f34ab3722e3afdd21301ca6cff4c4a
    CONTRACT_ABI=Use value from .env.docker.template
    PUBLIC_ADDRESS=Your public Ethereum address
    PRIVATE_KEY=Your private key
    ```
    Replace the placeholder values with your actual configuration details, such as your INFURA project ID, contract address, and Ethereum keys.

## Docker Setup

### Build and Start the Docker Containers

To build the Docker images and start the services, run:

```bash
docker-compose up --build
```
This command will build the Docker images and start the Django service along with a PostgreSQL database.

## Usage

After starting the Docker containers, you can access the API at [http://localhost:8000/](http://localhost:8000/).

## API Endpoints

### 1. Create Token

- **Endpoint:** `api/tokens/create`
- **Method:** `POST`
- **Request Parameters:**
  - `media_url`: URL of the media (string)
  - `owner`: Ethereum address of the token owner (string)
- **Response:** Returns the newly created Token object.

### 2. List Tokens

- **Endpoint:** `api/tokens/list`
- **Method:** `GET`
- **Response:** Returns a list of all Token objects.

### 3. Total Supply

- **Endpoint:** `api/tokens/total_supply`
- **Method:** `GET`
- **Response:** Returns the total supply of tokens from the blockchain.

## Additional Endpoints

- **Admin Panel:**  
  - **Endpoint:** `/admin`
  - **Description:** Access the Django admin interface.

- **Swagger Documentation:**  
  - **Endpoint:** `/swagger`
  - **Description:** View and interact with the API documentation via Swagger UI.

- **ReDoc Documentation:**  
  - **Endpoint:** `/redoc`
  - **Description:** Alternative API documentation with ReDoc.

- **API Authentication:**  
  - **Endpoint:** `/api-auth`
  - **Description:** Endpoints for obtaining and managing authentication tokens.

## Contributing

Feel free to submit issues or pull requests if you want to contribute to the project.



## NFT Backend Service (Сервис бэкенда NFT)

Этот проект представляет собой бэкенд-сервис, построенный на базе Django и Django REST Framework (DRF) для взаимодействия со смарт-контрактом ERC-721 NFT на блокчейне Ethereum (тестовая сеть Sepolia). Сервис позволяет создавать новые NFT и получать информацию о существующих NFT через REST API.

## Содержание

- [Функции](#функции)
- [Технологии](#технологии)
- [Установка](#установка)
- [Настройка](#настройка)
- [Настройка Docker](#настройка-docker)
- [Использование](#использование)
- [API-эндпоинты](#api-эндпоинты)
- [Контрибьютинг](#Контрибьютинг)

## Функции

- **Создание NFT:** Создание новых NFT путём взаимодействия со смарт-контрактом ERC-721.
- **Получение списка токенов:** Получение списка всех созданных токенов, хранящихся в базе данных.
- **Проверка общего количества:** Получение общего количества токенов из блокчейна.

## Технологии

- **Python 3.7+**
- **Django 4+**
- **Django REST Framework**
- **Web3.py**
- **PostgreSQL**
- **Docker**
- **Swagger** (drf-yasg)

## Установка

### Клонирование репозитория

```bash
git clone https://github.com/maximunya/test-nft.git
cd test-nft
```

## Настройка

1. Скопируйте файл `.env.docker.template` и переименуйте его в `.env.docker`:

    ```bash
    cp .env.docker.template .env.docker
    ```

2. Откройте файл `.env.docker` и заполните следующие переменные окружения:

    ```env
    SECRET_KEY=Ваш секретный ключ Django
    DEBUG=True
   
    DB_NAME=Название вашей базы данных
    DB_USER=Имя пользователя вашей базы данных
    DB_PASSWORD=Пароль вашей базы данных
    DB_HOST=Хост вашей базы данных
    DB_PORT=Порт вашей базы данных

    INFURA_URL=https://sepolia.infura.io/v3/ИД_ВАШЕГО_ПРОЕКТА_INFURA
    CONTRACT_ADDRESS=0x399c1448e0f34ab3722e3afdd21301ca6cff4c4a
    CONTRACT_ABI=Используйте значение из .env.docker.template
    PUBLIC_ADDRESS=Ваш публичный адрес Ethereum
    PRIVATE_KEY=Ваш секретный ключ
    ```
    Замените значения по умолчанию на ваши реальные конфигурационные данные, такие как ID вашего проекта Infura, адрес контракта, ключи Ethereum и т.д.

## Настройка Docker

### Сборка и запуск контейнеров Docker

Чтобы собрать образы Docker и запустить сервисы, выполните:

```bash
docker-compose up --build
```
Эта команда соберет образы Docker и запустит сервис Django вместе с базой данных PostgreSQL.

## Использование

После запуска контейнеров Docker вы можете получить доступ к API по адресу [http://localhost:8000/](http://localhost:8000/).

## API-эндпоинты

### 1. Создание токена

- **Эндпоинт:** `api/tokens/create`
- **Метод:** `POST`
- **Параметры запроса:**
  - `media_url`: URL медиа (string)
  - `owner`: Адрес Ethereum владельца токена (string)
- **Ответ:** Возвращает созданный объект Token.

### 2. Список токенов

- **Эндпоинт:** `api/tokens/list`
- **Метод:** `GET`
- **Ответ:** Возвращает список всех объектов Token.

### 3. Общее количество

- **Эндпоинт:** `api/tokens/total_supply`
- **Метод:** `GET`
- **Ответ:** Возвращает общее количество токенов из блокчейна.

## Дополнительные точки доступа

- **Панель администрирования:**  
  - **Эндпоинт:** `/admin`
  - **Описание:** Доступ к интерфейсу администрирования Django.

- **Документация Swagger:**  
  - **Эндпоинт:** `/swagger`
  - **Описание:** Документация API через Swagger UI.

- **Документация ReDoc:**  
  - **Эндпоинт:** `/redoc`
  - **Описание:** Альтернативная документация API с помощью ReDoc.

- **Аутентификация API:**  
  - **Эндпоинт:** `/api-auth`
  - **Описание:** Эндпоинт для получения и управления токенами аутентификации.






