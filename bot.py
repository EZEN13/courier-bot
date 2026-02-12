"""
Bot module.
Initializes and configures the Telegram bot.
"""

import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import config
from handlers import chat_router
from database.db import db
from services.openai_service import init_openai

logger = logging.getLogger(__name__)


async def on_startup() -> None:
    """Execute on bot startup."""
    logger.info("Starting bot...")

    # Connect to database
    await db.connect()
    logger.info("Database connected")

    # Initialize OpenAI client
    init_openai()
    logger.info("OpenAI client initialized")

    logger.info("Bot started successfully")


async def on_shutdown() -> None:
    """Execute on bot shutdown."""
    logger.info("Shutting down bot...")

    # Disconnect from database
    await db.disconnect()
    logger.info("Database disconnected")

    logger.info("Bot shutdown complete")


def create_bot() -> Bot:
    """Create and configure the bot instance."""
    return Bot(
        token=config.TELEGRAM_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )


def create_dispatcher() -> Dispatcher:
    """Create and configure the dispatcher."""
    dp = Dispatcher()

    # Register routers
    dp.include_router(chat_router)

    # Register startup/shutdown handlers
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    return dp
