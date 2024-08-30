# NFT Backend Service

This project is a backend service built using Django and Django REST Framework (DRF) to interact with an ERC-721 NFT smart contract on the Ethereum blockchain (Sepolia Testnet). The service allows you to mint new NFTs and retrieve information about existing NFTs via a REST API.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker Setup](#docker-setup)
- [Contributing](#contributing)
- [License](#license)

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
- **Swagger** (optional, for API documentation)

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/nft-backend-service.git
cd nft-backend-service
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
    CONTRACT_ABI=Your ABI JSON
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

## Accessing the API

After starting the Docker containers, you can access the API at [http://localhost:8000/](http://localhost:8000/).

## Usage

Once the Docker containers are up and running, you can interact with the API through the provided endpoints.

## API Endpoints

### 1. Create Token

- **Endpoint:** `/tokens/create`
- **Method:** `POST`
- **Request Parameters:**
  - `media_url`: URL of the media (string)
  - `owner`: Ethereum address of the token owner (string)
- **Response:** Returns the newly created Token object.

### 2. List Tokens

- **Endpoint:** `/tokens/list`
- **Method:** `GET`
- **Response:** Returns a list of all Token objects.

### 3. Total Supply

- **Endpoint:** `/tokens/total_supply`
- **Method:** `GET`
- **Response:** Returns the total supply of tokens from the blockchain.

## Contributing

Feel free to submit issues or pull requests if you want to contribute to the project.

