import asyncio
from Database.session import async_session
from Database.DAL.ChannelDAL import ChannelDAL
# async def mmm():
#     async with async_session() as session:
#         async with session.begin():
#             channels = ChannelDAL(session)
#             c = await channels.search_by_username("м", 1)
#             for i in c[0]:
#                 print(i)
#             print(c[1])
#
# asyncio.run(mmm())

async def mmm():
    async with async_session() as session:
        async with session.begin():
            channels = ChannelDAL(session)
            c = await channels.advertising_records_by_hours_chart()
            for i in c:
                print(i)

asyncio.run(mmm())