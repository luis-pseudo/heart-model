FROM python:3.8

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Entrenar el modelo dentro del contenedor con la versión correcta de scikit-learn/numpy
RUN python model/train.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
