FROM python:3.9-slim

WORKDIR /app
COPY train_model.py /app
RUN pip install fpgrowth-py pandas

CMD ["python", "train_model.py"]
