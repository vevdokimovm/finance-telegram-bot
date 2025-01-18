import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

# Создание бота и диспетчера
TOKEN = "<TOKEN>"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключение к базе данных
conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

# Создаём таблицу, если её нет
cursor.execute("""
CREATE TABLE IF NOT EXISTS finance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    type TEXT,
    amount REAL
)
""")
conn.commit()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я помогу тебе учесть доходы и расходы. Используй команды /income и /expense для добавления записей.")

# Обработчик для команды /income
@dp.message(Command("income"))
async def add_income(message: Message):
    try:
        args = message.text.split()
        if len(args) != 2 or not args[1].isdigit():
            await message.answer("Пожалуйста, введите сумму дохода в формате: /income 1000")
            return
        amount = float(args[1])
        cursor.execute("INSERT INTO finance (user_id, type, amount) VALUES (?, ?, ?)",
                       (message.from_user.id, "income", amount))
        conn.commit()
        await message.answer(f"Доход {amount} успешно добавлен!")
    except Exception as e:
        await message.answer("Произошла ошибка. Попробуйте снова.")
        print(e)

# Обработчик для команды /expense
@dp.message(Command("expense"))
async def add_expense(message: Message):
    try:
        args = message.text.split()
        if len(args) != 2 or not args[1].isdigit():
            await message.answer("Пожалуйста, введите сумму расхода в формате: /expense 500")
            return
        amount = float(args[1])
        cursor.execute("INSERT INTO finance (user_id, type, amount) VALUES (?, ?, ?)",
                       (message.from_user.id, "expense", -amount))
        conn.commit()
        await message.answer(f"Расход {amount} успешно добавлен!")
    except Exception as e:
        await message.answer("Произошла ошибка. Попробуйте снова.")
        print(e)

# Обработчик команды /summary
@dp.message(Command("summary"))
async def summary(message: Message):
    cursor.execute("SELECT SUM(amount) FROM finance WHERE user_id = ?",
                   (message.from_user.id,))
    total = cursor.fetchone()[0]
    total = total if total else 0
    await message.answer(f"Ваш текущий баланс: {total:.2f}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
