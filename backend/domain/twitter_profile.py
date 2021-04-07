class TwitterProfile:
    def __init__(self):
        self.profile_id = 0
        self.name = ""
        self.banner_image = ""
        self.profile_image = ""
        self.tweets = []

    def get_profile_id(self):
        return self.profile_id

    def get_name(self):
        return self.name

    def get_banner_image(self):
        return self.banner_image

    def get_profile_image(self):
        return self.profile_image

    def get_tweets(self):
        return self.tweets

    def set_profile_id(self, profile_id):
        self.profile_id = profile_id

    def set_name(self, name):
        self.name = name

    def set_banner_image(self, banner_image):
        self.banner_image = banner_image

    def set_profile_image(self, profile_image):
        self.profile_image = profile_image

    def set_tweets(self, tweets):
        self.tweets = tweets

    def __eq__(self, other):
        if self.name != other.get_name():
            return False
        if self.profile_image != other.get_profile_image():
            return False
        if self.banner_image != other.get_banner_image():
            return False
        if self.tweets != other.get_tweets():
            return False
        return True

    def __str__(self):
        return self.name + "\n" + str(self.tweets) + "\n" + self.profile_image + "\n" + self.banner_image
