"""
Memory service module.
Handles short-term memory operations for user conversations.
"""

from config import config
from database.db import db


async def save_message(user_id: int, role: str, content: str) -> int:
    """
    Save a message to the database.

    Args:
        user_id: Telegram user ID
        role: Message role ('user' or 'assistant')
        content: Message content

    Returns:
        ID of the saved message
    """
    return await db.save_message(user_id, role, content)


async def get_last_messages(user_id: int, limit: int = None) -> list[dict]:
    """
    Get the last N messages for a user.

    Args:
        user_id: Telegram user ID
        limit: Maximum number of messages (default from config)

    Returns:
        List of message dictionaries with role and content
    """
    if limit is None:
        limit = config.MEMORY_LIMIT
    return await db.get_last_messages(user_id, limit)


async def clear_history(user_id: int) -> int:
    """
    Clear conversation history for a user.

    Args:
        user_id: Telegram user ID

    Returns:
        Number of deleted messages
    """
    return await db.clear_user_history(user_id)
