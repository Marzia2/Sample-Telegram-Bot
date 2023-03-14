import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = ""
admins = []
bot = aiogram.Bot(token=token, parse_mode="HTML", validate_token=True)
storage = MemoryStorage()
