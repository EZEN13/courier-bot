# Telegram AI Consultant Bot для курьеров

AI-консультант для курьеров Яндекс Еда на базе Telegram и OpenAI.

## Возможности

- Ответы на вопросы курьеров на русском языке
- Интеграция с OpenAI GPT-4o-mini
- Короткая память (последние 15 сообщений на пользователя)
- Модульная архитектура
- Подготовка к интеграции векторной базы данных

## Структура проекта

```
courier-bot/
├── main.py              # Точка входа
├── config.py            # Конфигурация
├── bot.py               # Инициализация бота
├── handlers/
│   └── chat.py          # Обработчики сообщений
├── services/
│   ├── openai_service.py    # Интеграция с OpenAI
│   ├── memory_service.py    # Управление памятью
│   ├── prompt_service.py    # Системный промпт
│   └── vector_service.py    # Заготовка для векторной БД
├── database/
│   └── db.py            # SQLite операции
├── .env                 # Переменные окружения
├── requirements.txt     # Зависимости
└── README.md
```

## Установка

### 1. Клонирование / Переход в директорию

```bash
cd courier-bot
```

### 2. Создание виртуального окружения

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# или
venv\Scripts\activate     # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка .env файла

Откройте файл `.env` и добавьте ваш OpenAI API ключ:

```env
TELEGRAM_TOKEN=7969826382:AAFaY47ozWgFxjMnl8kKvK0PH8fpP9eZ3cM
OPENAI_API_KEY=sk-ваш-ключ-здесь
```

## Запуск

```bash
python main.py
```

## Команды бота

- `/start` - Начать общение
- `/clear` - Очистить историю диалога
- `/help` - Показать справку

## Тестирование

1. Запустите бота: `python main.py`
2. Откройте Telegram и найдите вашего бота
3. Отправьте `/start`
4. Задайте вопрос, например: "Как пройти фотоконтроль?"

## Конфигурация

Все настройки в файле `.env`:

| Переменная | Описание | По умолчанию |
|------------|----------|--------------|
| TELEGRAM_TOKEN | Токен Telegram бота | - |
| OPENAI_API_KEY | API ключ OpenAI | - |
| OPENAI_MODEL | Модель OpenAI | gpt-4o-mini |
| OPENAI_MAX_TOKENS | Макс. токенов в ответе | 1000 |
| OPENAI_TEMPERATURE | Температура генерации | 0.7 |
| MEMORY_LIMIT | Кол-во сообщений в памяти | 15 |
| DATABASE_PATH | Путь к базе данных | database/bot.db |

## Будущие улучшения

- [ ] Интеграция векторной базы данных (ChromaDB/Pinecone)
- [ ] RAG для расширенной базы знаний
- [ ] Логирование в файл
- [ ] Метрики и мониторинг
