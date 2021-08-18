import json

with open("stoic_sample.json", "r") as read_file:
    data = json.load(read_file)

for key in data:
    x = data.get(f"{key}", {}).get("title")
    print(key, x)


# TODO: parse loaded data by day and load into db