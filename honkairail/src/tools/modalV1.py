from pydantic import BaseModel
from typing import List,Optional


class Player(BaseModel):
    uid: str
    name: str
    level: int
    icon: str
    signature: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"


class RankIcon(BaseModel):
    icon: str
    unlock: bool

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class Skill(BaseModel):
    name: str
    level: int
    type: str
    icon: str
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class MainProperty(BaseModel):
    name: str
    value: str
    icon: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class SubProperty(BaseModel):
    name: str
    value: str
    icon: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class Relic(BaseModel):
    name: str
    rarity: int
    level: int
    main_property: MainProperty
    sub_property: List[SubProperty]
    icon: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class RelicSet(BaseModel):
    name: str
    icon: str
    desc: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class Property(BaseModel):
    name: str
    base: str
    addition: Optional[str]
    icon: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"

class PatchInfo(BaseModel):
    name: Optional[str]
    url: Optional[str]

class LightConeInfo(BaseModel):
    atk: Optional[int]
    hp: Optional[int]
    defense: Optional[int]
    patch: Optional[PatchInfo]

class LightCone(BaseModel):
    id: Optional[int]
    name: Optional[str]
    rarity: Optional[int]
    rank: Optional[int]
    level: Optional[int]
    icon: Optional[str] = "icon/light_cone/24000.png"
    portrait: Optional[str]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = self.icon.split('/')[2][:-4]
        portrait = self.icon.replace("icon/light_cone/", "image/light_cone_portrait/")
        self.portrait = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{portrait}"
        self.icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.icon}"
        

class Character(BaseModel):
    id: Optional[str]
    name: Optional[str]
    rarity: Optional[int]
    level: Optional[int]
    rank: Optional[int]
    rank_text: Optional[str]
    rank_icons: List[RankIcon]
    preview: Optional[str]
    portrait: Optional[str]
    path: Optional[str]
    path_icon: Optional[str]
    element: Optional[str]
    element_icon: Optional[str]
    color: Optional[str]
    skill: List[Skill]
    light_cone: Optional[LightCone]
    relic: dict[str, Relic]
    relic_set: List[RelicSet]
    property: List[Property]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = self.name.format(NICKNAME = "Trailblazer")
        self.element_icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.element_icon}"
        self.path_icon = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.path_icon}"
        self.preview = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.preview}"
        self.portrait = f"https://raw.githubusercontent.com/Mar-7th/StarRailRes/master/{self.portrait}"



class StarRailApiData(BaseModel):
    player: Player
    characters: List[Character]

class PlayerSpaceInfo(BaseModel):
    PassAreaProgress: Optional[int]
    LightConeCount: Optional[int]
    AvatarCount: Optional[int]
    AchievementCount: Optional[int]


class PlayerDetailInfo(BaseModel):
    UID: int
    CurFriendCount: Optional[int]
    WorldLevel: Optional[int]
    Signature: Optional[str]
    NickName: Optional[str]
    Birthday: Optional[int]
    Level: Optional[int]
    PlayerSpaceInfo: Optional[PlayerSpaceInfo]


class PlayerInfo(BaseModel):
    PlayerDetailInfo: PlayerDetailInfo
  

