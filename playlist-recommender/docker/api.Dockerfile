FROM python:3.9-slim

WORKDIR /app
COPY app.py /app
COPY playlist_rules.pkl /app
RUN pip install flask

CMD ["python", "app.py"]

