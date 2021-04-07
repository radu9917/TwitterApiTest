import unittest
from repository.twitter_profile_repo import TwitterProfileRepo
from domain.twitter_profile import TwitterProfile
from domain.tweet import Tweet


class ProfileRepoTest(unittest.TestCase):
    def test_repo(self):
        repo = TwitterProfileRepo()
        test_profile = TwitterProfile()
        test_profile.set_name("mariandistrugatorul69")
        test_profile.set_profile_image("https://mgedev.com/images/mge_logo.webp")
        test_profile.set_banner_image("https://mgedev.com/images/mge_logo.webp")
        test_tweet = Tweet()
        test_tweet.set_tweet_id("0123414")
        test_tweet.set_content("i was at walmart and it was decent")
        test_tweet.set_likes(420)
        test_tweet.set_responses(69)
        repo.store(test_profile)
        # Test Store and Get
        self.assertEqual(test_profile, repo.get(1))
        # Test Update, GetAll and Delete
        test_profile.set_tweets([test_tweet])
        repo.update(1, test_profile)
        self.assertEqual([test_profile], repo.get_all())



