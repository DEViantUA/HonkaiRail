# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['honkairail', 'honkairail.src', 'honkairail.src.tools']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'honkairail',
    'version': '1.0.0',
    'description': 'A simple and convenient model for Mihoyo API which is complemented by other resources',
    'long_description': '# HonkaiRail\n A simple and convenient model for Mihoyo API which is complemented by other resources\n\n\n## Install:\n\n```\npip install honkairail\n```\n\n## Uses:\n``` py\nfrom honkairail import starrailapi\nimport asyncio\n\nasync def main(uid,lang):\n    r = starrailapi.StarRailApi(lang)\n    data = await r.get_full_data(uid)\n    print(data)\n\nasyncio.run(main(700649319,"en"))\n```\n\n## Usage example:\n\n```py\nfrom honkairail import starrailapi\nimport asyncio\n\n\nasync def main(uid,lang):\n    r = starrailapi.StarRailApi(lang)\n    data = await r.get_full_data(uid)\n    print("====Player====")\n    print(f"Name: {data.player.name}")\n    print(f"UID: {data.player.uid}")\n    print(f"Level: {data.player.level}")\n    print(f"World Level: {data.player.worldlevel}")\n    \n    print(f"Birthday: {data.player.birthday}")\n    print(f"Friends: {data.player.friends}")\n\n    print(f"Pass Area Progress: {data.player.pass_area_progress}")\n    print(f"Achievement: {data.player.achievement}")\n\n    print(f"Characters: {data.player.characters}")\n    print(f"Light Cone: {data.player.light_cone}")\n\n    print(f"Icon: {data.player.icon}")\n    print(f"Signature: {data.player.signature}")\n    print(\'\\n\\n\')\n    print("====Characters====")\n    for character in data.characters:\n        print(f"Name: {character.name} | {character.id}")\n        print(f"Rarity: {\'★\'*character.rarity}")\n        print(f"LVL: {character.level}")\n        print(f"===={character.rank_text}====")\n        for rank in character.rank_icons:\n            print(f"Icon: {rank.icon}\\nUnlock: {rank.unlock}")\n        print("====Skill====")\n        for skill in character.skill:\n            print(f"Icon: {skill.icon}\\nLVL:{skill.level}")\n        print("=============")\n        if not character.light_cone is None:\n            print(f"Light Cone: {character.light_cone.name}")\n            print(f"Rarity: {\'★\'*character.light_cone.rarity}")\n            print(f"LVL: {character.light_cone.level} | R{character.light_cone.rank}")\n            print(f"Icon: {character.light_cone.icon}")\n            print(f"Portrait: {character.light_cone.portrait}")\n            light_cone = await r.get_light_cone_info(character.light_cone)\n            print(f"ATK: {light_cone.atk} | HP: {light_cone.hp} | DEF: {light_cone.defense}")\n            print(f"Path: {light_cone.patch.name}\\nImage: {light_cone.patch.url}")\n        print("====Stats====")\n        for property in character.property:\n            if property.addition is None:\n                print(f"{property.name}: {property.base}\\nIcon: {property.icon}")\n            else:\n                print(f"{property.name}: {property.base} ({property.addition})\\n==Icon: {property.icon}")\n        print(\'\\n\\n\')\n        print("====Relic====")\n        for i in character.relic:\n            print(f"{character.relic[i].name}: {character.relic[i].level} lvl | {\'★\'*character.relic[i].rarity}")\n            print(f"{character.relic[i].main_property.name}: {character.relic[i].main_property.value}")\n            for sub_property in character.relic[i].sub_property:\n                print(f"=={sub_property.name}: {sub_property.value}\\n====Icon: {sub_property.icon}")\n            print(\'\\n\')\n        print("\\n\\n")\n\nasyncio.run(main(700649319, "en"))\n```\n\n\n### Languages Supported\n| Languege    |  Code   | Languege    |  Code   | Languege    |  Code   |\n|-------------|---------|-------------|---------|-------------|---------|\n|  English    |     en  |  русский    |     ru  |  Chinese    |    chs  |\n|  Tiếng Việt |     vi  |  ไทย        |     th  | Taiwan     |    cn  |\n|  português  |     pt  | 한국어      |     kr  | deutsch    |     de  |\n|  日本語      |     jp  | 中文        |     zh  | español    |     es  |\n|  中文        |     zh  | Indonesian |     id  | français   |     fr  |\n\n',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/DEViantUA/HonkaiRail',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
