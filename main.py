"""
Main entry point for the Telegram AI Consultant Bot.
"""

import asyncio
import logging
import sys

from config import config
from bot import create_bot, create_dispatcher


def setup_logging() -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )


async def main() -> None:
    """Main function to run the bot."""
    setup_logging()
    logger = logging.getLogger(__name__)

    # Validate configuration
    if not config.validate():
        logger.error("Configuration validation failed. Exiting.")
        sys.exit(1)

    # Create bot and dispatcher
    bot = create_bot()
    dp = create_dispatcher()

    logger.info("Starting polling...")

    try:
        # Start polling
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped by user")
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
