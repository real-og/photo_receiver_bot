from loader import dp
from aiogram import types, filters
from aiogram.dispatcher import FSMContext
import texts
from loader import ADMIN_IDS
from logic import upload_all_files
import time

@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.welcome)


@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_id) in ADMIN_IDS:
        await message.answer(texts.help_admin)
    else:
        await message.answer(texts.help)


@dp.message_handler(filters.IDFilter(chat_id=ADMIN_IDS), commands=['stash'])
async def send_welcome(message: types.Message, state: FSMContext):
    folder_name = message.text[7:]
    if folder_name == '':
        await message.answer(texts.folder_name_needed)
        return
    await message.answer(texts.uploading_started)
    upload_all_files(folder_name)


    
    
