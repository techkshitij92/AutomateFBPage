import praw
import creds
reddit = praw.Reddit(
    client_id = credss.client_id,
    client_secret = creds.client_secret,
    password = creds.password,
    user_agent = creds.user_agent,
    username = creds.username,
    redirect_uri = creds.redirect_uri,
)
print(reddit.auth.url(scopes=["identity"], state="...", duration="permanent"))
print(reddit.user.me())

subreddit = reddit.subreddit("programmer")
for submission in subreddit.hot(limit=25):
    print(submission.title)
