import requests


class Post:

    def __init__(self):
        self.response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        self.all_posts = self.response.json()

    def title(self):
        all_title = []
        for i in range(3):
            title = self.all_posts[i]["title"]
            all_title.append(title)
        return all_title

    def subtitle(self):
        all_subtitle = []
        for i in range(3):
            subtitle = self.all_posts[i]["subtitle"]
            all_subtitle.append(subtitle)
        return all_subtitle

    def body(self):
        all_body = []
        for i in range(3):
            body = self.all_posts[i]["body"]
            all_body.append(body)
        return all_body


