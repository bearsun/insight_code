import pandas as pd
import requests
import time
import datetime

def get_data(after, before):
	"""
	get all submission within a time window from pushshift, by default pushshift only return 25 entries/page

	input
	-----
	int after: machine time for the start of the time window
	int before: machine time for the end of the time window

	output
	-----
	list: a list of data downloaded, each element is a dictionary
	"""

    url = 'https://api.pushshift.io/reddit/search/submission/?after='+str(after)+'&before='+str(before)+'&subreddit=nba'
    data = None
    while data is None:
        try:
            data = requests.get(url).json()
        except:
        	# some time the server doesn't return anything, then we wait and try again
            print('wait for server...')
            time.sleep(10)
    return data['data']

def collectSubData(subm):
	"""
	transform a dictionary to an entry in pandas dataframe

	input
	-----
	dict subm: a dictionary with different fields of the data entry

	output
	-----
	pd.df: a single entry pandas dataframe with data
	"""

    subData = pd.DataFrame(data = [[subm['id'], subm['title'], subm['author'], subm['author_flair_text'],
                                   datetime.datetime.fromtimestamp(subm['created_utc']),
                                   subm['num_comments']]],
                           columns = ['id', 'title', 'author', 'flair', 'created', 'ncomments'])
    return subData

def main():
	'''
	pushshift has a nice feature which we can scrap threads by time (praw removed this feature one year ago).
	so here we use pushshift to scrap all threads posted during the 18-19 NBA regular seasons with their thread ids
	as a directory to scrap all data later with praw.
	'''

	# define the start/end time of our scraping, e.g. the whole 18-19 NBA regular season
	after = int(time.mktime(datetime.datetime.strptime('10/16/2018','%m/%d/%Y').timetuple()))
	before = int(time.mktime(datetime.datetime.strptime('4/10/2019','%m/%d/%Y').timetuple()))

	# download data, there is a 25 entries limit per page, so we need a loop
	data = get_data(after, before)
	ds = pd.DataFrame()
	while len(data) > 0: #until no more data left within the time window
    	for submission in data:
    		# transform each entry into the pandas dataframe
        	subData = collectSubData(submission)
        	ds = ds.append(subData, ignore_index = True)
        # monitor the progress of scraping
    	print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
    	# update the start time to scrap the next 25 entries
    	after = data[-1]['created_utc']
    	data = get_data(after, before)
    # save to csv
	ds.to_csv('nba_submissions_reg18.csv')
	print(ds.shape)


if __name__ == "__main__":
	main()