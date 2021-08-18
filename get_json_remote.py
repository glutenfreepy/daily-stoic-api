import requests
URL = "https://raw.githubusercontent.com/IshanMi/Stoicbot/master/pdf_parsing/Stoic_log.json"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    # TODO: load data into Deta Base (key, stoic_title)
    for key in data:
        stoic_title = data.get(f"{key}", {}).get("title")
        print(key, stoic_title)
        # db.put({"title": f'"{stoic_title}"'}, {"key": f'"{key}"'})
else:
    break