import aiohttp
import asyncio
import json
from .modalV1 import StarRailApiData
from .modalV2 import StarRailApiDataV2
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

API_LINK = "https://api.mihomo.me/sr_info_parsed/{uid}?lang={lang}&version=v1"
API_LINK_V2 = "https://api.mihomo.me/sr_info_parsed/{uid}?lang={lang}"
FULL_API_LINK = "https://api.mihomo.me/sr_info/{uid}?lang={lang}&version=v1"
LIGHT_CONES_LINK = "https://mana.wiki/starrail/collections/lightCones/{id}?_data=_custom%2Froutes%2F%24siteId.collections%2B%2FlightCones_.%24entryId"

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if "detail" in data:
                raise TypeError(data["detail"])
            return data

async def get_user_data(uid, lang, v):
    lang = SUPPORTED_LANGUAGES.get(lang.lower(), "en")
    if v == 1:
        url = API_LINK.format(uid=uid, lang=lang)
    else:
        url = API_LINK_V2.format(uid=uid, lang=lang)
    return await fetch_data(url)

async def get_full_user_data(uid, lang):
    lang = SUPPORTED_LANGUAGES.get(lang.lower(), "en")
    url = FULL_API_LINK.format(uid=uid, lang=lang)
    return await fetch_data(url)

async def get_light_cones_data(id):
    url = LIGHT_CONES_LINK.format(id=id)
    return await fetch_data(url)

async def get_data(lang, uid, v):
    data = await get_user_data(uid, lang, v)
    if v == 1:
        return StarRailApiData(player=data["player"], characters=data["characters"])
    return StarRailApiDataV2(player=data["player"], characters=data["characters"])

async def get_full(lang, uid,v):
    data = await get_user_data(uid, lang,v)
    for key in data["characters"]:
        if key["light_cone"] == {}:
            key["light_cone"] = None
    if v == 1:
        profile = await get_full_user_data(uid,lang)
        player_info = profile["detailInfo"]
        data["player"]["friends"] = player_info["friendCount"]
        data["player"]["worldlevel"] = player_info["worldLevel"]
        data["player"]["birthday"] = "0"#utilities.convert_date(profile["Birthday"])
        data["player"]["pass_area_progress"] = player_info["recordInfo"]["challengeInfo"]["scheduleMaxLevel"]
        data["player"]["light_cone"] = player_info["recordInfo"]["equipmentCount"]
        data["player"]["characters"] = player_info["recordInfo"]["avatarCount"]
        data["player"]["achievement"] = player_info["recordInfo"]["achievementCount"]

        return StarRailApiData(player=data["player"], characters=data["characters"])
    return StarRailApiDataV2(player=data["player"], characters=data["characters"])


    