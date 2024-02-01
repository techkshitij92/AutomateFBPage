import praw
import cred
reddit = praw.Reddit(
    client_id = cred.client_id,
    client_secret = cred.client_secret,
    password = cred.password,
    user_agent = cred.user_agent,
    username = cred.username,
    redirect_uri = cred.redirect_uri,
)
print(reddit.auth.url(scopes=["identity"], state="...", duration="permanent"))
print(reddit.user.me())

subreddit = reddit.subreddit("programmer")
for submission in subreddit.hot(limit=25):
    print(submission.title)
