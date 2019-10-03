import praw
import pandas as pd
import time


def get_history(user, reddit):
    '''
    get the history (subreddits posted recently) for a user

    input
    -----
    str user: an user name
    obj reddit: the reddit object from praw

    output
    -----
    pd.df: one entry with all subreddit names concatenated
    '''

    # request a user object from praw
    redditor = reddit.redditor(name=user)

    # start scraping
    cnt = 0
    subs = ''
    try:
        # concatenate all subreddit names for one user
        for comment in redditor.comments.new(limit=None):
            subs += ' ' + comment.subreddit.display_name
            cnt += 1
    except BaseException:
        # in case praw doesn't like me
        print('wait for server...')
        time.sleep(10)

    # pack in an entry
    entry = pd.DataFrame([[user, subs, cnt]], columns=[
                         'user', 'history', 'count'])
    return entry


def main():
    '''
    scrap each user's visiting history by praw, specifically,
    which subreddits the user posted comments recently (max=1000)
    '''

    # usernames/user_ids extracted from previously scraped comments
    authors = pd.read_csv('authors.csv')
    # start a bot to scrap
    # see
    # https://praw.readthedocs.io/en/latest/getting_started/authentication.html
    reddit = praw.Reddit('bot1')

    # start scraping
    ds = pd.DataFrame()
    n = authors.shape[0]
    i = 0
    for user in authors:
        i += 1
        ds = ds.append(get_history(user, reddit), ignore_index=True)
        # print progress every 100 entries
        if i % 100 == 0:
            print(str(i / n * 100) + '%')

    # output to csv
    ds.to_csv('bot1_final.csv')


if __name__ == '__main__':
    main()
