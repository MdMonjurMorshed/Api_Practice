FROM python:3.8-slim as builder

ENV PYTHONBUFFERED=1
WORKDIR /app
COPY requirements.txt /app
COPY . /app
RUN pip install -r requirements.txt

FROM python:3.8-slim
ENV PYTHONBUFFERED=1
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
WORKDIR /app
COPY . . 

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
