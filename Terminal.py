#!/usr/bin/env python3
import typer
from rich.console import Console
from Track import getUserTweets

console = Console()

def userTweet(user: str, count: int, replies: bool, retweets: bool):
    commentWith = "Including"
    if replies == True:
        commentWith = "Excluding"

    retweetWith = "Including"
    if retweets == False:
        retweetWith = "Excluding"

    typer.echo(console.print(
        (f"[bold blue]::[/bold blue][bold violet] Serching {count} Past Tweets of [/ bold violet][bold yellow]{user.capitalize()}[/ bold yellow] [bold violet]{commentWith} Comments and {retweetWith} Retweets[/ bold violet]")))

    getUserTweets(user, count, replies, retweets)


if __name__ == "__main__":
    typer.run(userTweet)
