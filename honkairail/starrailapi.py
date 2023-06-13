from .src.tools import api, modalV1,utilities

class StarRailApi():
    def __init__(self,lang, v = 1) -> None:
        self.lang = lang
        if not v in [1,2]:
            v = 1
        self.v = v

    async def get_user(self,uid):
        data = await api.get_data(self.lang,uid,self.v)
        return data
    
    async def get_user_profile(self,uid):
        data = await api.get_profile(self.lang,uid)
        return data
    
    async def get_full_data(self,uid):
        data = await api.get_full(self.lang,uid,self.v)
        return data
    
    async def get_light_cone_info(self, instance):
        stats = await api.get_light_cones_data(instance.id)
        data = utilities.get_stats_light_cone(stats["defaultData"]["stats_csv"], instance.level)
        patch = stats["defaultData"]["path"]
        icon = patch["icon"]
        data["patch"] = {
            "name": patch["name"],
            "url": icon["url"]
        }
        return modalV1.LightConeInfo(**data)