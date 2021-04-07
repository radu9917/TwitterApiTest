from repository.repo_interface import IRepo
import copy


class TweetRepo(IRepo):
    def __init__(self):
        self.tweet_list = []
        self.id = 1

    def store(self, tweet):
        self.tweet_list.append(copy.deepcopy(tweet))

    def delete(self, tweet_id):
        for tweet in self.tweet_list:
            if tweet_id == tweet.get_tweet_id():
                self.tweet_list.remove(tweet)

    def update(self, old_tweet_id, new_profile):
        for tweet in self.tweet_list:
            if old_tweet_id == tweet.get_tweet_id():
                new_profile.set_tweet_id(old_tweet_id)
                self.delete(old_tweet_id)
                self.store(new_profile)

    def get_all(self):
        return copy.deepcopy(self.tweet_list)

    def get(self, tweet_id):
        for tweet in self.tweet_list:
            if tweet_id == tweet.get_tweet_id():
                return copy.deepcopy(tweet)
