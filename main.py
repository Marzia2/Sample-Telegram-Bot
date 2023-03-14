import asyncio
import config
from Bot.dispatcher import XDispatcher
from database.Base import Base, engine


async def startup():
    ...


async def main():
    Base.metadata.create_all(bind=engine)
    asyncio.create_task(startup())
    x_dispatcher = XDispatcher(bot=config.bot)
    await x_dispatcher.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
