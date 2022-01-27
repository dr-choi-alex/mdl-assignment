FROM python:3.7

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./src/openapi_server /app

WORKDIR /app

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]