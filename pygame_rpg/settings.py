import json

default_settings = {
    "scale": 2,
    "name": "player"
}

class Settings:

    def __init__(self):

        try:
            with open("settings.json", "r") as s:
                self.data = json.load(s)
        except FileNotFoundError: # no settings
            print("no settings.json")

            with open("settings.json", "w") as s:
                json.dump(default_settings, s)
                self.data = json.load(s)
            