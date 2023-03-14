import config
import aiogram
from aiogram import Dispatcher
from Bot.Profile.Handler import Handler as ProfileHandler
from Bot.filters import IsAdmin


class XDispatcher(object):
    def __init__(self, bot: aiogram.Bot):
        self.bot = bot
        self.dp = Dispatcher(bot, storage=config.storage)
        self.handler_profile = ProfileHandler(self)
        self.__register_filters()
        self.__register_middleware()
        self.__register_events()

    def __register_filters(self):
        self.dp.filters_factory.bind(IsAdmin)

    def __register_middleware(self):
        ...

    def __register_events(self):
        self.handler_profile.register_commands_event(), self.handler_profile.register_state_event(),
        self.handler_profile.register_message_event(), self.handler_profile.register_callback_event()


    async def start_polling(self):
        print(f"---[@{(await self.bot.get_me()).username}]Бот успешно запущен---")
        return await self.dp.start_polling()
