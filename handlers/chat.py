"""
Chat handler module.
Handles incoming Telegram messages.
"""

import logging
from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart, Command

from services.memory_service import save_message, get_last_messages, clear_history
from services.openai_service import generate_response
from services.prompt_service import get_system_message, get_welcome_message, get_registration_url

logger = logging.getLogger(__name__)

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message) -> None:
    """Handle /start command - send welcome and save to memory."""
    user_id = message.from_user.id

    # Clear old history for fresh start
    await clear_history(user_id)

    # Send welcome message with registration button
    welcome = get_welcome_message()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="РЕГИСТРАЦИЯ ↗️",
            url=get_registration_url()
        )]
    ])
    await message.answer(welcome, reply_markup=keyboard)

    # Save welcome as assistant message so AI remembers it
    await save_message(user_id, "assistant", welcome)


@router.message(Command("clear"))
async def handle_clear(message: Message) -> None:
    """Handle /clear command - clear conversation history."""
    user_id = message.from_user.id
    deleted = await clear_history(user_id)
    await message.answer(f"История очищена. Удалено сообщений: {deleted}")


@router.message(Command("help"))
async def handle_help(message: Message) -> None:
    """Handle /help command."""
    help_text = (
        "🤖 Команды бота:\n\n"
        "/start - Начать общение\n"
        "/clear - Очистить историю диалога\n"
        "/help - Показать эту справку\n\n"
        "Просто напишите свой вопрос, и я постараюсь помочь!"
    )
    await message.answer(help_text)


@router.message(F.text)
async def handle_message(message: Message) -> None:
    """Handle incoming text messages."""
    user_id = message.from_user.id
    user_text = message.text

    if not user_text:
        return

    try:
        # Show typing indicator
        await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")

        # Save user message
        await save_message(user_id, "user", user_text)

        # Get conversation history
        history = await get_last_messages(user_id)

        # Build messages for OpenAI
        messages = [get_system_message()]
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})

        # Generate response
        response_text = await generate_response(messages)

        # Save assistant response
        await save_message(user_id, "assistant", response_text)

        # Send response to user
        await message.answer(response_text)

    except Exception as e:
        logger.error(f"Error handling message from user {user_id}: {e}")
        await message.answer(
            "Извините, произошла ошибка. Пожалуйста, попробуйте позже."
        )


@router.message()
async def handle_other(message: Message) -> None:
    """Handle non-text messages."""
    await message.answer(
        "Извините, я могу обрабатывать только текстовые сообщения. "
        "Пожалуйста, напишите ваш вопрос текстом."
    )
