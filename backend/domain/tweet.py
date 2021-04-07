class Tweet:
    def __init__(self):
        self.content = ""
        self.likes = 0
        self.responses = 0
        self.tweet_id = "0"

    def get_content(self):
        return self.content

    def get_likes(self):
        return self.likes

    def get_responses(self):
        return self.responses

    def get_tweet_id(self):
        return self.tweet_id

    def set_content(self, content):
        self.content = content

    def set_likes(self, likes):
        self.likes = likes

    def set_responses(self, responses):
        self.responses = responses

    def set_tweet_id(self, tweet_id):
        self.tweet_id = tweet_id

    def __eq__(self, other):
        if self.tweet_id != other.get_tweet_id():
            return False
        if self.likes != other.get_likes():
            return False
        if self.responses != other.get_responses():
            return False
        if self.content != other.get_content():
            return False
        return True
