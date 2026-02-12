"""
Configuration module for the Telegram AI Consultant Bot.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration."""

    # Telegram
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN", "")

    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    OPENAI_MAX_TOKENS: int = int(os.getenv("OPENAI_MAX_TOKENS", "1000"))
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))

    # Memory
    MEMORY_LIMIT: int = int(os.getenv("MEMORY_LIMIT", "15"))

    # Database
    DATABASE_PATH: str = os.getenv("DATABASE_PATH", "database/bot.db")

    @classmethod
    def validate(cls) -> bool:
        """Validate required configuration."""
        if not cls.TELEGRAM_TOKEN:
            print("Error: TELEGRAM_TOKEN is not set")
            return False
        if not cls.OPENAI_API_KEY:
            print("Error: OPENAI_API_KEY is not set")
            return False
        return True


config = Config()
