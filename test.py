import requests
import json

class API: #make request
    def __init__(self):
        self.url = "https://www.magetic.com/c/test?api=1&amp;name=ann_martynenko"
        self.response = requests.get(self.url)

class get_games_name():
    def __init__(self, response):
        self.content = response.content.decode("utf-8").split(';') #decode content of the page
        self.game_numb = len(self.content) - 1 #count games

    def __str__(self):
        return str(self.game_numb)

class build_jason():
    def __init__(self, content, game_numb):
        self.result = []
        self.number = 1
        self.content = content
        self.game_numb = game_numb

    def build(self): #make data in json format
        for x in self.content:
            if self.number > self.game_numb: break
            self.result.append({"gamename": x, "number" : self.number})
            self.number += 1

class print_json():
    def __init__(self, result):
        self.result = result
    def make_file(self): #put json data to file
        with open('data.txt', 'w') as outfile:
            json.dump(self.result, outfile)
    def __str__(self):
        return str(self.result)

connect = API()
game_names = get_games_name(connect.response)
print("Number of games: ", game_names)
json_data = build_jason(game_names.content, game_names.game_numb)
json_data.build()
res = print_json(json_data.result)
res.make_file()
print(json.dumps(json_data.result, indent=4, sort_keys=True))