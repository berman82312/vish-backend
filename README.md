# Vish
Internal tools built by Fish.

## Prerequitises

1. uv package manager

This project use [uv](https://docs.astral.sh/uv/) as package manager.

2. mysql client

We use MySQL as our database. Please refer to [mysqlclient](https://pypi.org/project/mysqlclient/) and follow the instructions to install mysql client on your system. Django requires this client to communicate with the database.

## How to run this project

1. Setup `.env` file

```bash
cp .env.example .env
```

2. Generate a secret key

You can visit [Djecrety](https://djecrety.ir/) to generate a secure secret key. Copy and paste it to your `.env` file.
