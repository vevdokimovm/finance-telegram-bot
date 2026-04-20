# TG-bot-for-finances

A Telegram bot for tracking personal income and expenses, built with Python and aiogram 3.

## Features

- Add income records with `/income <amount>`
- Add expense records with `/expense <amount>`
- View current balance with `/summary`
- Per-user data isolation via Telegram user ID
- Persistent storage using SQLite

## Tech Stack

- Python 3.10+
- [aiogram 3](https://docs.aiogram.dev/) — async Telegram Bot API framework
- SQLite — local database for transaction storage

## Getting Started

### Prerequisites

- Python 3.10 or higher
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

### Installation

```bash
git clone https://github.com/vevdokimovm/TG-bot-for-finances.git
cd TG-bot-for-finances
pip install -r requirements.txt
```

### Configuration

Open `bot_with_database.py` and replace `<TOKEN>` with your Telegram bot token:

```python
TOKEN = "your_telegram_bot_token_here"
```

### Run

```bash
python bot_with_database.py
```

## Bot Commands

| Command | Description |
|---|---|
| `/start` | Welcome message and usage instructions |
| `/income <amount>` | Add an income record (e.g. `/income 5000`) |
| `/expense <amount>` | Add an expense record (e.g. `/expense 1200`) |
| `/summary` | Show current balance |

## License

MIT
