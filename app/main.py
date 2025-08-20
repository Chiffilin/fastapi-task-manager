# app/main.py

from contextlib import asynccontextmanager

from fastapi import FastAPI

# Удаляем импорт create_tables, т.к. миграция будет выполняться отдельно
from app.db.database import engine

# Импортируем роутер
from app.routers.tasks import router


# Асинхронный контекстный менеджер для обработки событий жизненного цикла приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Обрабатывает события жизненного цикла приложения.
    Выполняется при запуске и завершении работы.
    """
    # Действия при запуске (теперь без создания таблиц)
    yield
    # Действия при завершении работы
    print("Закрытие подключения к базе данных...")
    engine.dispose()


app = FastAPI(lifespan=lifespan)

# Включаем роутер
app.include_router(router)
