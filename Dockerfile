FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./config /root/.aws/config

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
