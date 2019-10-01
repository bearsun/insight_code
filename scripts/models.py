import pandas as pd
from load_data import load_data, load_history
from teamname_stdize import teamname_stdize
from preprocess import preprocess_one
from ner import ner
from sklearn.model_selection import train_test_split
from textrank import textrank
from mvp import mvp
from model2 import model2
from model3 import model3
from model4 import model4

def custom_normalize(np_data):
	'''
	normalize log_proba from each model before adding them together
	for the ensemble model

	input
	-----
	np.array np_data: log_proba of sample X team

	output
	-----
	np.array: array scaled by min/max
	'''
    mx = np_data.max()
    mn = np_data.min()
    return (np_data-mn)/(mx-mn)

def main():

	# load threads/comments data
	ds_orig = load_data()

	# standerdize team names into abbreviations (3 letters, e.g. TOR)
	ds = teamname_stdize(ds_orig)

	# preprocess texts
	ds['text'] = ds['text'].apply(lambda x: preprocess_one(x, True))

	# preprocessed texts (keep punctuation)
	prep_text = ds['text'].apply(lambda x: preprocess_one(x, False)).to_frame()

	# Named Entity Recognition
	ds = ds.join(ner(prep_text))

	# drop all entries without entities
	ds_sub = ds.loc[ds['entity'].notnull(),:]

	# concat all texts by users
	ds_user = ds_sub.groupby(['author', 'team'])['text'].apply(lambda x: ' '.join(x)).reset_index()

	# concat all entities by users
	ds_user_ents = ds_sub.groupby(['author', 'team'])['entity'].apply(lambda x: ' '.join(x)).reset_index()

	# put together
	ds_user = ds_user.join(ds_user_ents['entity'])

	# load history data
	ds_history = load_history()

	# join to the main table
	ds_all = ds_user.merge(ds_history, how = 'left', left_on = 'author', right_on = 'user')

	# drop users with not history
	ds_all.dropna(inplace = True)

	# split to train/test by 80/20
	X_train, X_test, y_train, y_test = train_test_split(ds_all[['text', 'entity', 'history']], 
                                                    ds_all['team'], test_size=0.20, random_state=0)

	# MVP model: comment data + tf-idf + SMOTE + Multinomial Naive Bayes
	tfidf_smote_nb, log_proba_m1 = mvp(X_train, X_test, y_train, y_test)

	# model 2: entity data + tf-idf + SMOTE + Multinomial Naive Bayes
	log_proba_m2 = model2(X_train, X_test, y_train, y_test)

	# build corpus for textrank to process
	corpus = ' '.join(prep_text['text'].to_list())
	f = open('txt_corpus.txt', 'w')
	f.write(corpus)
	f.close()

	# run textrank
	textrank()

	# model 3: entity data + textrank + SMOTE + Multinomial Naive Bayes
	log_proba_m3 = model3(X_train, X_test, y_train, y_test)

	# model 4:
	log_proba_m4 = model4(X_train, X_test, y_train, y_test)

	# now put the four models together for an ensemble model
	pred_comb = custom_normalize(log_proba_m1) + custom_normalize(log_proba_m2)
	+ custom_normalize(log_proba_m3) + custom_normalize(log_proba_m4)

	y_comb = y_test.to_frame().copy()
	y_comb['pred'] = tfidf_smote_nb.classes_[pred_comb.argmax(axis = 1)]
	y_comb['cor'] = y_comb['pred'] == y_comb['team']
	print('Ensemble model')
	print('Testing acc:')
	print(y_comb['cor'].mean())

if __name__ == '__main__':
	main()