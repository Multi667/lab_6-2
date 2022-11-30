import json
from typing import List
INPUT_FILE = "input.csv"


def csv_to_list_dict(INPUT_FILE, delimiter = ',', new_line ='\n') -> List[dict]:
    final = []

    with open(INPUT_FILE) as file:
        lines = file.read().split(new_line)

        for i in range(1, len(lines)):
            func = {lines[0].split(delimiter)[k]: lines[i].split(delimiter)[k] for k in range(len(lines[i].split(delimiter)))}
            final.append(func)

    return final


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
