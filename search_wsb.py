from psaw import PushshiftAPI
import datetime
api = PushshiftAPI()

start_time = int(datetime.datetime(2021, 1, 30).timestamp())

submissions = list(api.search_submissions(after=start_time, subreddit='wallstreetbets', \
    filter=['url', 'author', 'title', 'subreddit'], limit=50))

for submission in submissions:
    # print(submission)
    print("\n")
    # print(submission.created_utc)
    # print(submission.title)
    # print(submission.url)

    words = submission.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

    if len(cashtags) > 0:
        print(cashtags)
        # print(submission.created_utc)
        print(submission.title)
        # print(submission.url)
    else:
        print('not found')