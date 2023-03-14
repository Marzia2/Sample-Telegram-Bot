import random
import string
from datetime import datetime
import pytz
from aiogram import types


def is_(callback: types.CallbackQuery, is_: str, split_: str = None) -> bool:
    if split_:
        return callback.data.split(split_)[0] == is_
    else:
        return callback.data == is_


def moscow_time():
    return datetime.now(pytz.timezone('Europe/Moscow'))


def generate_id(length: int):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))
