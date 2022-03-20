from json import dump, load

with open("data.json", "w") as f:
    f.write(dump(
        {
            "name" : "jugg",
            "url" : "../haha.com"
        }
    ))