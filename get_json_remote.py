import requests
URL = "https://raw.githubusercontent.com/IshanMi/Stoicbot/master/pdf_parsing/Stoic_log.json"

# TODO: check for valid response and only proceed if valid
data = requests.get(URL).json()

# TODO: load data into Deta Base (key, stoic_title)
for key in data:
    stoic_title = data.get(f"{key}", {}).get("title")
    print(key, stoic_title)
    # db.put({"title": f'"{stoic_title}"'}, {"key": f'"{key}"'})
