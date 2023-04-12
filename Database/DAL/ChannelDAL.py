# from sqlalchemy import and_
# from sqlalchemy import select
# from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from Database.Models.ChannelModel import Channel


class ChannelDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_channel(
            self,
            id_channel: int,
            name: str, link: str,
            avatar_url: str,
            description: str,
            subs_total: int
    ) -> Channel:

        new_channel = Channel(
            id_channel=id_channel,
            name=name,
            link=link,
            avatar_url=avatar_url,
            description=description,
            subs_total=subs_total
        )
        self.db_session.add(new_channel)
        await self.db_session.flush()
        return new_channel

    # async def delete_user(self, user_id: UUID) -> Union[UUID, None]:
    #     query = (
    #         update(User)
    #         .where(and_(User.user_id == user_id, User.is_active == True))
    #         .values(is_active=False)
    #         .returning(User.user_id)
    #     )
    #     res = await self.db_session.execute(query)
    #     deleted_user_id_row = res.fetchone()
    #     if deleted_user_id_row is not None:
    #         return deleted_user_id_row[0]
    #
    # async def get_user_by_id(self, user_id: UUID) -> Union[User, None]:
    #     query = select(User).where(User.user_id == user_id)
    #     res = await self.db_session.execute(query)
    #     user_row = res.fetchone()
    #     if user_row is not None:
    #         return user_row[0]
    #
    # async def update_channel_simple(self, user_id: UUID, **kwargs) -> Union[UUID, None]:
    #     query = (
    #         update(User)
    #         .where(and_(User.user_id == user_id, User.is_active == True))
    #         .values(kwargs)
    #         .returning(User.user_id)
    #     )
    #     res = await self.db_session.execute(query)
    #     update_user_id_row = res.fetchone()
    #     if update_user_id_row is not None:
    #         return update_user_id_row[0]