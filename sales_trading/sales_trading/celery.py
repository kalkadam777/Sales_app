import os
from celery import Celery

# Устанавливаем переменную окружения для Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sales_trading.settings")

app = Celery("sales_trading")

# Загружаем настройки из Django settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматически искать таски в Django-приложениях
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
