import praw

bot = praw.Reddit(user_agent='whenIsFirefly v0.1',
                  client_id='kHTToC7jHEp61A',
                  client_secret='VDk2Vrddpwa7cBLTFutbh8f4N7w',
                  username='WhenIsFireflyBot',
                  password='fairys')

subreddit = bot.subreddit('scriptBotTesting')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'when is firefly' in text.lower():
        # Generate a message
        message = "Hey, u/{0}, Firefly is June 20th to the 23rd, 2019. Beep Boop!".format(author)

        comment.reply(message) # Send message
