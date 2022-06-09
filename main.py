from aiogram import types
from config import bot, dp
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.reply("Hello World")
    await bot.send_message(message.chat.id, "Hello im your first bot")



@dp.message_handler(commands=['quiz_1'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая викторина",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Смог ли ты решить задачу ?"
    answers = [
            "Да",
            "Нет",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type = "quiz",
        correct_option_id=0,
        explanation="Решение задачи в файле problem1\!",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call:types.CallbackQuery):
    markup1 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следующая викторина",
                                         callback_data="button_call_2")
    markup1.add(button_call_2)
    question = "Какая из следующих функций преобразует строку в список в Python?"
    answers = [
        "list(mystring)",
        "tuple(mystring)",
        "eval(mystring)",
        "repr(mystring)"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation="This is easy, not gonna explain\!",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup = markup1
    )
@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call:types.CallbackQuery):
    markup2 = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следующая викторина",
                                         callback_data="button_call_3")
    markup2.add(button_call_3)

    question = "Как получить данные от пользователя"
    answers = [
        "cin()",
        "get()",
        "input()",
        "read()"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        explanation="This is easy, not gonna explain\!",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup2
    )
@dp.callback_query_handler(lambda call: call.data == "button_call_3")
async def quiz_4(call:types.CallbackQuery):
    question = "Где правильно создана переменная?"
    answers = [
        "%num = 2",
        "num = 2",
        "int num = 2",
        "var num = 2"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        explanation="This is easy, not gonna explain\!",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
