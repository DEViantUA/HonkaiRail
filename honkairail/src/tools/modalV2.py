from . import utilities
from pydantic import BaseModel
from typing import List,Optional

class Color(BaseModel):
    hex: Optional[str]
    rgba: Optional[tuple]

class ElementV2(BaseModel):
    id: Optional[str]
    name: Optional[str]
    color: Optional[str]
    icon: Optional[str]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"
        self.color = Color(hex = self.color, rgba = utilities.hex_to_rgba(self.color))

class SkillV2(BaseModel):
    id: Optional[str]
    name: Optional[str]
    level: Optional[int]
    max_level: Optional[int]
    element: Optional[ElementV2]
    type: Optional[str]
    type_text: Optional[str]
    effect: Optional[str]
    effect_text: Optional[str]
    simple_desc: Optional[str]
    desc: Optional[str]
    icon: Optional[str]

class PathV2(BaseModel):
    id: Optional[str]
    name: Optional[str]
    icon: Optional[str]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class AttributeV2(BaseModel):
    field: Optional[str]
    name: Optional[str]
    icon: Optional[str]
    value: Optional[float]
    display: Optional[str]
    percent: Optional[bool]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class PropertyV2(BaseModel):
    type: Optional[str]
    field: Optional[str]
    name: Optional[str]
    icon: Optional[str]
    value: Optional[float]
    display: Optional[str]
    percent: Optional[bool]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class LightConeV2(BaseModel):
    id: Optional[str]
    name: Optional[str]
    rarity: Optional[int]
    rank: Optional[int]
    level: Optional[int]
    promotion: Optional[int]
    icon: Optional[str] = "icon/light_cone/24000.png"
    preview: Optional[str]
    portrait: Optional[str]
    path: Optional[PathV2] 
    attributes: Optional[List[AttributeV2]]
    properties: Optional[List[PropertyV2]]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portrait = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.portrait}"
        self.preview = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.preview}"
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class AffixV2(BaseModel):
    type: Optional[str]
    field: Optional[str]
    name: Optional[str]
    icon: Optional[str]
    value: Optional[float]
    display: Optional[str]
    percent: Optional[bool]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class RelicV2(BaseModel):
    id: Optional[str]
    name: Optional[str]
    set_id: Optional[str]
    set_name: Optional[str]
    rarity: Optional[int]
    level: Optional[int]
    icon: Optional[str]
    main_affix: Optional[AffixV2]
    sub_affix: Optional[List[AffixV2]]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class PropertyV2(BaseModel):
    type: Optional[str]
    field: Optional[str]
    name: Optional[str]
    icon: Optional[str]
    value: Optional[float]
    display: Optional[str]
    percent: Optional[bool]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class RelicSetV2(BaseModel):
    id: str
    name: str
    desc: str
    properties: Optional[List[PropertyV2]]


class Addition(BaseModel):
    field: str
    name: str
    icon: str
    value: float
    display: str
    percent: bool

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class SkillTrees(BaseModel):
    id: Optional[int]
    level: Optional[int]
    icon: Optional[str]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class CharacterData(BaseModel):
    id: Optional[str]
    name: Optional[str]
    rarity: Optional[int]
    rank: Optional[int]
    level: Optional[int]
    promotion: Optional[int]
    icon: Optional[str]
    preview: Optional[str]
    portrait: Optional[str]
    path: Optional[PathV2]
    rank_icons: Optional[list]
    element: Optional[ElementV2]
    skills: Optional[List[SkillV2]]
    skill_trees: Optional[List[SkillTrees]]
    light_cone: Optional[LightConeV2]
    relics: Optional[List[RelicV2]]
    relic_sets: Optional[List[RelicSetV2]]
    additions: Optional[List[Addition]]
    attributes: Optional[List[AttributeV2]]
    properties: Optional[List[PropertyV2]]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = self.name.format(NICKNAME = "Trailblazer")
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"
        self.preview = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.preview}"
        self.portrait = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.portrait}"
        new_rank_icons = []
        for key in self.rank_icons:
            new_rank_icons.append(f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{key}")
        self.rank_icons = new_rank_icons



class Avatar(BaseModel):
    id: Optional[str]
    name: Optional[str]
    icon: Optional[str]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class SpaceInfo(BaseModel):
    pass_area_progress: Optional[int]
    light_cone_count: Optional[int]
    avatar_count: Optional[int]
    achievement_count: Optional[int]

class PlayerV2(BaseModel):
    uid: Optional[str]
    nickname: Optional[str]
    level: Optional[int]
    avatar: Optional[Avatar]
    signature: Optional[str]
    friend_count: Optional[int]
    world_level: Optional[int]
    birthday: Optional[str]
    space_info: Optional[SpaceInfo]

class StarRailApiDataV2(BaseModel):
    player: PlayerV2
    characters: List[CharacterData]