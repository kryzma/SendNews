FROM python:3.10

COPY . .

RUN pip install -r requirements.txt

ENV PORT=8080

EXPOSE 8080

cmd ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]