FROM python:3.11-slim

WORKDIR /usr/src/app

COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

RUN mkdir -p /usr/src/app/static

COPY . .

RUN chmod -R 755 /usr/src/app/static

EXPOSE 8000

WORKDIR /usr/src/app/sales_trading

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]