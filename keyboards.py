from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts

begin_quest_kb = ReplyKeyboardMarkup([[texts.begin_quest_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)
