import aiohttp
import asyncio
import json
from .modal import StarRailApiData, PlayerInfo
from . import utilities

SUPPORTED_LANGUAGES = {
    'cht': 'cht',
    'cn': 'cn',
    'de': 'de',
    'en': 'en',
    'es': 'es',
    'fr': 'fr',
    'id': 'id',
    'jp': 'jp',
    'kr': 'kr',
    'pt': 'pt',
    'ru': 'ru',
    'th': 'th',
    'vi': 'vi'
}

API_LINK = "https://api.mihomo.me/sr_info_parsed/{uid}?lang={lang}"
FULL_API_LINK = "https://api.mihomo.me/sr_info/{uid}?lang={lang}"
LIGHT_CONES_LINK = "https://mana.wiki/starrail/collections/lightCones/{id}?_data=_custom%2Froutes%2F%24siteId.collections%2B%2FlightCones_.%24entryId"

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if "detail" in data:
                raise TypeError(data["detail"])
            return data

async def get_user_data(uid, lang):
    lang = SUPPORTED_LANGUAGES.get(lang.lower(), "en")
    url = API_LINK.format(uid=uid, lang=lang)
    return await fetch_data(url)

async def get_full_user_data(uid, lang):
    lang = SUPPORTED_LANGUAGES.get(lang.lower(), "en")
    url = FULL_API_LINK.format(uid=uid, lang=lang)
    return await fetch_data(url)

async def get_light_cones_data(id):
    url = LIGHT_CONES_LINK.format(id=id)
    return await fetch_data(url)

async def get_data(lang, uid):
    data = await get_user_data(uid, lang)
    return StarRailApiData(player=data["player"], characters=data["characters"])

async def get_profile(lang, uid):
    data = await get_full_user_data(uid, lang)
    player_info = PlayerInfo(**data)
    return player_info.PlayerDetailInfo

async def get_full(lang, uid):
    profile, data = await asyncio.gather(get_profile(lang, uid), get_user_data(uid, lang))
    profile = json.loads(profile.json())

    for key in data["characters"]:
        if key["light_cone"] == {}:
            key["light_cone"] = None

    player_info = profile["PlayerSpaceInfo"]
    data["player"]["friends"] = profile["CurFriendCount"]
    data["player"]["worldlevel"] = profile["WorldLevel"]
    data["player"]["birthday"] = utilities.convert_date(profile["Birthday"])
    data["player"]["pass_area_progress"] = player_info["PassAreaProgress"]
    data["player"]["light_cone"] = player_info["LightConeCount"]
    data["player"]["characters"] = player_info["AvatarCount"]
    data["player"]["achievement"] = player_info["AchievementCount"]
    
    return StarRailApiData(player=data["player"], characters=data["characters"])


    