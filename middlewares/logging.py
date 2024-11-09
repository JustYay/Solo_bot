from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject
from loguru import logger


class UserActivityMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user_id = None
        username = None
        action = None

        if isinstance(event, Message):
            user_id = event.from_user.id
            username = event.from_user.username
            action = f"Сообщение: {event.text}"
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id
            username = event.from_user.username
            action = f"Обратный вызов: {event.data}"

        # Логируем действие пользователя
        logger.info(
            f"Активность пользователя - "
            f"ID пользователя: {user_id}, "
            f"Имя пользователя: {username}, "
            f"Действие: {action}"
        )

        # Продолжаем выполнение обработчика
        return await handler(event, data)
