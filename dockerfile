FROM python:3.12.3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ['python','-m','uvicorn','fastapi_app:app','--reload']