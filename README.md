# HonkaiRail
 A simple and convenient model for Mihoyo API which is complemented by other resources


## Install:

```
pip install honkairail
```

## Uses:
``` py
from honkairail import starrailapi
import asyncio

#The sample code below matches version 1 (v = 1), but you can set it to 1 or 2. The second version is newer and contains a bit more data.
async def main(uid,lang):
    r = starrailapi.StarRailApi(lang, v = 1)
    data = await r.get_full_data(uid)
    print(data)

asyncio.run(main(700649319,"en"))
```

## Usage example:

```py
from honkairail import starrailapi
import asyncio


async def main(uid,lang):
    r = starrailapi.StarRailApi(lang)
    data = await r.get_full_data(uid)
    print("====Player====")
    print(f"Name: {data.player.name}")
    print(f"UID: {data.player.uid}")
    print(f"Level: {data.player.level}")
    print(f"World Level: {data.player.worldlevel}")
    
    print(f"Friends: {data.player.friends}")

    print(f"Pass Area Progress: {data.player.pass_area_progress}")
    print(f"Achievement: {data.player.achievement}")

    print(f"Characters: {data.player.characters}")
    print(f"Light Cone: {data.player.light_cone}")

    print(f"Icon: {data.player.icon}")
    print(f"Signature: {data.player.signature}")
    print('\n\n')
    print("====Characters====")
    for character in data.characters:
        print(f"Name: {character.name} | {character.id}")
        print(f"Rarity: {'★'*character.rarity}")
        print(f"LVL: {character.level}")
        print(f"===={character.rank_text}====")
        for rank in character.rank_icons:
            print(f"Icon: {rank.icon}\nUnlock: {rank.unlock}")
        print("====Skill====")
        for skill in character.skill:
            print(f"Icon: {skill.icon}\nLVL:{skill.level}")
        print("=============")
        if not character.light_cone is None:
            print(f"Light Cone: {character.light_cone.name}")
            print(f"Rarity: {'★'*character.light_cone.rarity}")
            print(f"LVL: {character.light_cone.level} | R{character.light_cone.rank}")
            print(f"Icon: {character.light_cone.icon}")
            print(f"Portrait: {character.light_cone.portrait}")
            light_cone = await r.get_light_cone_info(character.light_cone)
            print(f"ATK: {light_cone.atk} | HP: {light_cone.hp} | DEF: {light_cone.defense}")
            print(f"Path: {light_cone.patch.name}\nImage: {light_cone.patch.url}")
        print("====Stats====")
        for property in character.property:
            if property.addition is None:
                print(f"{property.name}: {property.base}\nIcon: {property.icon}")
            else:
                print(f"{property.name}: {property.base} ({property.addition})\n==Icon: {property.icon}")
        print('\n\n')
        print("====Relic====")
        for i in character.relic:
            print(f"{character.relic[i].name}: {character.relic[i].level} lvl | {'★'*character.relic[i].rarity}")
            print(f"{character.relic[i].main_property.name}: {character.relic[i].main_property.value}")
            for sub_property in character.relic[i].sub_property:
                print(f"=={sub_property.name}: {sub_property.value}\n====Icon: {sub_property.icon}")
            print('\n')
        print("\n\n")

asyncio.run(main(700649319, "en"))
```


### Languages Supported
| Languege    |  Code   | Languege    |  Code   | Languege    |  Code   |
|-------------|---------|-------------|---------|-------------|---------|
|  English    |     en  |  русский    |     ru  |  Chinese    |    chs  |
|  Tiếng Việt |     vi  |  ไทย        |     th  | Taiwan     |    cn  |
|  português  |     pt  | 한국어      |     kr  | deutsch    |     de  |
|  日本語      |     jp  | 中文        |     zh  | español    |     es  |
|  中文        |     zh  | Indonesian |     id  | français   |     fr  |

