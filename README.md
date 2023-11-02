<img src = "https://raw.githubusercontent.com/DEViantUA/HonkaiRail/main/HonkaiRail.png" with = 100%> 

# HonkaiRail
 A simple and convenient model for Mihoyo API which is complemented by other resources


## Install:

```
pip install honkairail
```
___
* [Example](https://github.com/DEViantUA/HonkaiRail/tree/main/Example)
* [PyPi](https://pypi.org/project/honkairail/#files)
* [Discord HSR Server](https://discord.gg/eu55vTgmSA)
___

## Uses:
``` py
from honkairail import starrailapi
import asyncio

async def main(uid,lang):
    r = starrailapi.StarRailApi(lang, v = 2)
    data = await r.get_full_data(uid)
    print(data)

asyncio.run(main(700649319,"en"))
```

### Languages Supported
| Languege    |  Code   | Languege    |  Code   | Languege    |  Code   |
|-------------|---------|-------------|---------|-------------|---------|
|  English    |     en  |  русский    |     ru  |  Chinese    |    chs  |
|  Tiếng Việt |     vi  |  ไทย        |     th  | Taiwan     |    cn  |
|  português  |     pt  | 한국어      |     kr  | deutsch    |     de  |
|  日本語      |     jp  | 中文        |     cn  | español    |     es  |
|  中文        |     zh  | Indonesian |     id  | français   |     fr  |
| Український | ua |
