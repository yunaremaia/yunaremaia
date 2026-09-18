FROM python:3.11-slim

WORKDIR /app

COPY generate_streak.py .

CMD ["python", "generate_streak.py"]
