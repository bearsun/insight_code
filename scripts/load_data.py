import pandas as pd

def load_data():
	'''
	load both threads and comments and then concatenate them together

	input
	-----
	None

	output
	-----
	pd.df ds: dataset with author, team, text, created
	'''

	dir_data = '../data/nba_reg18/'

	ds_sub = pd.DataFrame()
	ds_com = pd.DataFrame()

	nf_subs = 7 #7 files for submissions
	nf_coms = 12 #12 files for comments

	# load threads
	for icom in range(1, nf_subs+1):
	    path_ds = dir_data + 'nba_submissions_reg18_' + str(icom) + '.csv'
	    ds_cur = pd.read_csv(path_ds, index_col = 0, parse_dates = ['created'])
	    ds_sub = ds_sub.append(ds_cur).drop_duplicates()

	# load comments
	for icom in range(1, nf_coms+1):
	    path_ds = dir_data + 'nba_comments_reg18_' + str(icom) + '.csv'
	    ds_cur = pd.read_csv(path_ds, index_col = 0, parse_dates = ['created'])
	    ds_com = ds_com.append(ds_cur).drop_duplicates()

	# put submissions and comments together
	ds = pd.concat([ds_sub[['author', 'flair', 'title', 'created']].rename(columns = {'flair':'team', 'title':'text'}),
	                ds_com[['author', 'flair', 'text', 'created']].rename(columns = {'flair':'team'})],
	               ignore_index = True)

	# drop empty texts
	ds.dropna(inplace = True)

	return ds

def load_history():
	'''
	load which subreddits user posted comments previously

	input
	-----
	None

	output
	-----
	pd.df ds_history: a dataframe with author and all subreddits they posted comments
	'''
	
	ds_history = pd.DataFrame()
	nfiles = 5 #scraped in 5 files 1~5
	for i in range(1,nfiles+1):
	    ds_bot = pd.read_csv('bot'+str(i)+'_final.csv', index_col = 0)
	    ds_history = ds_history.append(ds_bot)
	return ds_history