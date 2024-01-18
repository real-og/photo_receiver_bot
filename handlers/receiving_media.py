from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from aiogram import types
from aiogram.utils.exceptions import FileIsTooBig
from loader import ADMIN_IDS
from datetime import datetime


@dp.message_handler(state="*", content_types=types.ContentType.ANY)
async def send_welcome(mes: types.Message, state: FSMContext):
    if mes.content_type in ['photo', 'document', 'video']:
        try:
            if mes.photo:
                await mes.photo[-1].download(destination_file=f'buffer_files/{mes.message_id}.jpg')
            elif mes.video:
                await mes.video.download(destination_file=f'buffer_files/{mes.message_id}.mp4')
            elif mes.document:
                await mes.document.download(destination_dir=f'buffer_files/')

        except FileIsTooBig:
            """Resending file if it bigger than 20MB"""
            
            for id in ADMIN_IDS:
                print(id)
                try:
                    await mes.send_copy(id)
                except:
                    pass

        await mes.reply(texts.received)
    else:
        await mes.reply(texts.type_error)