from rich.console import Console
import tweepy
import re

console = Console()


# Variable
apiKey = "MEbNbcJEIyirnZCiW7zwyghFb"
apiKeySecret = "87laCFEu4qvkrsStT2lDKXp7aaLM8ACT43Jv63J9lAj6wj88Nq"
tokenKey = "1358061039225507841-ErJQsvkmr5ipgCUrGWKDaSVrbd5FmB"
tokenKeySecret = "kA2SXO8k308M08eMQCFTJFXTmxVvEZjGAidMIviS8PN2f"

# Authentication
auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
auth.set_access_token(tokenKey, tokenKeySecret)
api = tweepy.API(auth)


def getUserTweets(User, Count, Comment, Retweets):
    userTimeline = api.user_timeline(
        screen_name=User, count=Count, exclude_replies=Comment, include_rts=Retweets, tweet_mode="extended")
    for tweets in userTimeline:
        console.print(f"[bold blue]{tweets.created_at}[/bold blue] : {cleantext(tweets.full_text)} \n")

def cleantext(text):
    text = re.sub(r"@[A-Za-z0-9]+", "", text) # Remove Mentions
    text = re.sub(r"#", "", text) # Remove Hashtags Symbol
    text = re.sub(r"RT[\s]:+", "", text) # Remove Retweets
    text = re.sub(r"https?:\/\/\S+", "", text) # Remove The Hyper Link
    
    return text
