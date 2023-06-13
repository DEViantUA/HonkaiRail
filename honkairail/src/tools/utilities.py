def get_stats_light_cone(string, lvl):
    if lvl is None:
        return {"atk": 0, "hp": 0, "defense": 0}
    lines = string.split("<br/>")
    headers = lines[0].split(",")

    result_dict = {}

    for line in lines[1:]:
        values = line.split(",")
        
        if len(headers) != len(values):
            continue
        
        level = values[0]
        entry = {headers[i].lower(): int(float(values[i])) for i in range(1, len(headers))}
        if "def" in entry:
            entry["defense"] = entry.pop("def")
        
        result_dict[level] = entry

    if lvl == 0:
        lvl = 1

    return result_dict.get(str(lvl), {"atk": 0, "hp": 0, "defense": 0})

def hex_to_rgba(hex_code):
    hex_code = hex_code.strip('#')
    
    red = int(hex_code[0:2], 16)
    green = int(hex_code[2:4], 16)
    blue = int(hex_code[4:6], 16)
    
    alpha = 255 
    
    return red, green, blue, alpha


def convert_date(date):
    date = str(date)
    month = date[:-2].zfill(2)
    day = date[-2:].zfill(2)
    converted_date = f"{month}.{day}"
    return converted_date