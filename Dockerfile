FROM python:3.10-slim 
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src /app/src 
COPY ./models /app/models
EXPOSE 8080
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080" ]