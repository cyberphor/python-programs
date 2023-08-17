import pandas as pd

columns = ["tweet_id", "content"]
tweets = [
    [1, "Vote for Biden"],
    [1, "Let us make America great again!"],
]

df = pd.DataFrame(columns = columns, data = tweets)
invalid = df.loc[df['content'].str.len() < 15]
invalid[["tweet_id"]]

"""
| tweet_id | content                          |
| -------- | -------------------------------- |
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
"""

"""
return tweets.loc[tweets['content'].str.len() > 15][["tweet_id"]]
"""