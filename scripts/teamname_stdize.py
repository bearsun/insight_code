import pandas

def team2abbr(flair, team_dict, team_fulls, team_abbrs):
	'''
	transform a flair (e.g. full team name, player name with team abbr)
	into a team abbr

	input
	-----
	str flair: the original flair
    dict team_dict: mapping from a full team name to an abbr
    list team_fulls: list of full team names
	list team_abbrs: list of team abbrs (3 letters)

	output
	-----
	str flair: a new flair in the corresponding team abbr
	'''

    # if the flair is a full team name
    for name in team_fulls:
        if name in flair:
            return team_dict[name]
    
    # if a player name is in the flair, only return the team abbr
    for abbr in team_abbrs:
        if abbr in flair:
            return abbr
    
    # otherwise return original
    # (weired flairs will be bind into others later)
    return flair

def teamname_stdize(ds):
	'''
	standerdize all teamnames/flairs into 3 letters,
	e.g. TOR, LAL, BOS

	input
	-----
	pd.df ds: a dataframe with column 'flair'

	output:
	pd.df: a dataframe with standerdized teamnames
	'''

	team_names = pd.read_csv('teams', names = ['name', 'abbrs'])
	team_dict = team_names.set_index('name').to_dict()['abbrs']
	team_fulls = team_names['name'].to_list()
	team_abbrs = team_names['abbrs'].to_list()

	# get rid of the weired pandas float nan
	ds.loc[ds['team'].isnull().values, 'team'] = 'NONE'

	# mapping to abbrev team name
	ds['team'] = ds['team'].apply(team2abbr,
		args = [team_dict, team_fulls, team_abbrs])

	return ds