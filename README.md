# mdl-assignment

## Requirements
 + Docker
 + docker-compose
 + python 3.7+
 + fastAPI
 + angular 7

## How to run mdl-Assignment service 

1. git clone https://github.com/dr-choi-alex/mdl-assignment.git
    
2. Setting environment in docker-compose.yaml

    version: '3.6'
        services:
            api:
                build:
                context: ./backend
                dockerfile: ./Dockerfile
                environment:
                - ORIGINS_URL=http://localhost,http://localhost:80
                - DB_USERNAME=postgres
                - DB_PASSWORD=postgres
                - DB_HOST=localhost
                - DB_PORT=5432
                - DB_NAME=postgres
                ports:
                - "8000:8000"
                command: uvicorn main:app --host 0.0.0.0 --port 8000

            web:
                build:
                context: ./frontend
                dockerfile: ./Dockerfile
                ports:
                - "80:80"
                depends_on:
                - api

    
3.docker-compose up --build