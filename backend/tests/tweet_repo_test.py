import unittest
from repository.tweet_repo import TweetRepo
from domain.tweet import Tweet


class TweetRepoTest(unittest.TestCase):
    def test_repo(self):
        repo = TweetRepo()
        test_tweet = Tweet()
        test_tweet.set_tweet_id("0123414")
        test_tweet.set_content("i was at walmart and it was decent")
        test_tweet.set_likes(420)
        test_tweet.set_responses(69)
        repo.store(test_tweet)
        # Test Store and Get
        self.assertEqual(test_tweet, repo.get("0123414"))
        # Test Update, GetAll and Delete
        test_tweet.set_content("ami place sa mananc")
        repo.update("0123414", test_tweet)
        self.assertEqual([test_tweet], repo.get_all())



