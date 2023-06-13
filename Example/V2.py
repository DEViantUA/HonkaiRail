from honkairail import starrailapi
import asyncio


async def main(uid,lang):
    r = starrailapi.StarRailApi(lang, v = 2)
    data = await r.get_full_data(uid)
    print(data)

asyncio.run(main(700649319, "en"))
