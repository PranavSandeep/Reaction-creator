import json

__author__ = "Pranav Sandeep"

# importing data_file.json
UserConfig = json.load(open("UserConfig.json", "r"))


class UserSettings:
    def __init__(self):
        pass

    sentences = UserConfig["sentences"]
