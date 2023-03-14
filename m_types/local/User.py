import config
from database.models.User import User as MUser
from typing import Union
from contextlib import closing
from database.Base import SessionLocal


class AsyncActionDdUser:
    def __init__(self, id: int):
        self.__id = id

    @staticmethod
    async def db_create(**kwargs) -> MUser:
        with closing(SessionLocal()) as db:
            u = MUser(**kwargs)
            db.add(u), db.commit(), db.refresh(u)
            return u

    async def db_get(self) -> Union[MUser, None]:
        with closing(SessionLocal()) as db:
            return db.query(MUser).filter(MUser.id == self.__id).first()

    async def db_update(self, **kwargs) -> int:
        with closing(SessionLocal()) as db:
            db_query = db.query(MUser).filter(MUser.id == self.__id).update(kwargs)
            db.commit()
            return db_query

    async def db_delete(self):
        with closing(SessionLocal()) as db:
            db_query = db.query(MUser).filter(MUser.id == self.__id).delete()
            db.commit()
            return db_query


class User(AsyncActionDdUser):

    def __init__(self, id: int):
        self.__id = id
        super().__init__(id=self.__id)

    async def get_telegram_object(self):
        return await config.bot.get_chat(chat_id=self.__id)
