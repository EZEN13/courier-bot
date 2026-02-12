"""
OpenAI service module.
Handles communication with OpenAI API.
"""

import logging
from openai import AsyncOpenAI

from config import config

logger = logging.getLogger(__name__)

# Initialize OpenAI client
client: AsyncOpenAI = None


def init_openai() -> None:
    """Initialize the OpenAI client."""
    global client
    client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)


async def generate_response(messages: list[dict]) -> str:
    """
    Generate a response from OpenAI.

    Args:
        messages: List of message dictionaries with 'role' and 'content'

    Returns:
        Generated response text
    """
    global client

    if client is None:
        init_openai()

    try:
        response = await client.chat.completions.create(
            model=config.OPENAI_MODEL,
            messages=messages,
            max_tokens=config.OPENAI_MAX_TOKENS,
            temperature=config.OPENAI_TEMPERATURE,
        )

        return response.choices[0].message.content or "Извините, не удалось сгенерировать ответ."

    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        return "Извините, произошла ошибка при обработке запроса. Пожалуйста, попробуйте позже."
