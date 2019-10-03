import praw
import pandas as pd
import datetime
import time


def scan_thread(submission):
    '''
    scan a thread to read the submission(thread) and all comments under it

    input
    -----
    obj submission: praw object for submission

    output
    -----
    pd.df ds_sub: the submission entry
    pd.df ds: all comments entries
    '''

    # add the submission itself
    if submission.author is None:  # when the original thread was deleted
        ds_sub = pd.DataFrame()
    else:
        ds_sub = pd.DataFrame(
            data=[
                [
                    submission.id,
                    submission.title,
                    submission.author.name,
                    submission.author_flair_text,
                    datetime.datetime.fromtimestamp(
                        submission.created_utc),
                    submission.selftext]],
            columns=[
                'id',
                'title',
                'author',
                'flair',
                'created',
                'text'])

    # now go through the comments
    ds = pd.DataFrame()
    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:]
    for comment in comment_queue:
        if comment.author is None:  # if the author is missing, pass
            continue
        entry = pd.DataFrame(
            data=[
                [
                    comment.id,
                    comment.author.name,
                    comment.author_flair_text,
                    datetime.datetime.fromtimestamp(
                        comment.created_utc),
                    comment.body,
                    comment.parent_id]],
            columns=[
                'id',
                'author',
                'flair',
                'created',
                'text',
                'parent'])
        ds = ds.append(entry, ignore_index=True)

    return ds_sub, ds


def main():
    '''
    code to scrap all data (threads + comments) through praw,
    using submission (thread) ids from pushshift.
    '''

    # config in ~/.config/praw.ini
    # see
    # https://praw.readthedocs.io/en/latest/getting_started/authentication.html
    reddit = praw.Reddit('bot1')

    # load the thread ids scraped from pushshift
    # they are the roots for all comments
    subs = pd.read_csv('nba_submissions_reg18.csv', usecols=['id'])

    # start scraping
    ds_sub = pd.DataFrame()
    ds = pd.DataFrame()
    fsub_count = 1
    fcom_count = 1
    sub_count = 0

    tstart = time.time()
    for sub_id in subs['id']:
        sub_count += 1

        # keep track of the progress/speed (every 1000 threads)
        if sub_count % 1000 == 1:
            print(sub_count)
            tcur = time.time()
            # time lasted for every 1000 threads in minutes
            print(round((tcur - tstart) / 60, 2))
            tstart = tcur

        # scrap each thread and all comments under it
        sub = reddit.submission(id=sub_id)
        single_sub, single_ds = scan_thread(sub)
        ds_sub = ds_sub.append(single_sub, ignore_index=True)
        ds = ds.append(single_ds, ignore_index=True)

        # save every 200k comments into one file
        if ds.shape[0] > 200000:
            fname = 'nba_comments_reg18_' + str(fcom_count) + '.csv'
            print(fname)
            ds.to_csv(fname)
            fcom_count += 1
            ds = pd.DataFrame()

        # save every 200k threads into one file
        if ds_sub.shape[0] > 200000:
            fname = 'nba_submissions_reg18_' + str(fsub_count) + '.csv'
            print(fname)
            ds_sub.to_csv(fname)
            fsub_count += 1
            ds_sub = pd.DataFrame()

    # save the last pieces of data
    ds.to_csv('nba_comments_reg18_' + str(fcom_count) + '.csv')
    ds_sub.to_csv('nba_submissions_reg18_' + str(fsub_count) + '.csv')


if __name__ == '__main__':
    main()
