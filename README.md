# py-fastapi-clean-arch
Python clean architecture structure with FastAPI

## Requirements

For development, you will only need Python 3.8.7, PostgresSQL and Docker(Optional) installed in your environment.

### Python
- #### Python installation

  Just go on [official python website](https://www.python.org/downloads/) follow the installation process.

If the installation was successful, you should be able to run the following command.

    $ python --version
    v3.8.7

## Install

    $ git clone https://github.com/MatSLima/py-fastapi-clean-arch.git
    $ cd py-fastapi-clean-arch/
    $ pip install -r requirements.txt

## Configure env vars

Open the file with the name `.env.example` and save it with the name `.env`:

## Running the project (Multiple ways):
- #### Running by uvicorn (python)

      $ uvicorn app.main:app --reload

        or

      $ make run

- #### Running by Docker

      $ docker build -t py-fastapi-clean-arch .
      $ docker run --network host --env-file .env -d -p 8000:8000 py-fastapi-clean-arch

        or

      $ make build-docker
      $ make run-docker

- #### Running by Docker Compose

      $ docker-compose up -d

## Accessing API    
    `http://127.0.0.1:8000/docs`
