FROM python:3.10-slim
WORKDIR /app
COPY backend/app ./app
COPY backend/firebase-auth.json .
COPY backend/requirements.txt .
COPY backend/run.py .
COPY frontend/templates ./app/templates
COPY frontend/static ./app/static
RUN pip install -r requirements.txt
CMD ["python", "run.py"]