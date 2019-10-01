from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE
from cal_auc import cal_auc

def mvp(X_train, X_test, y_train, y_test):
	'''
	mvp model: text data + tf-idf + SMOTE + multinomialNB

	input
	-----
	pd.df X_train: training text
	pd.df X_test: testing text
	pd.df y_train: training labels
	pd.df y_test: testing labels

	output
	-----
	obj: the naive bayes model object
	np.array log_proba: log probability of prediction
	'''
	
	# tf-idf
	tfidf = TfidfVectorizer(max_features=3000,
		ngram_range=(1, 1), stop_words='english', max_df=.6)
	train_txt = tfidf.fit_transform(X_train['text'])
	test_txt = tfidf.transform(X_test['text'])

	# SMOTE
	X_train_resampled, y_train_resampled = SMOTE(random_state=0).fit_resample(train_txt, y_train)

	# Naive Bayes
	tfidf_smote_nb = MultinomialNB()
	tfidf_smote_nb.fit(X_train_resampled, y_train_resampled)

	# predict
	print('MVP model')
	print('training acc:')
	print(tfidf_smote_nb.score(train_txt, y_train))

	print('testing acc:')
	print(tfidf_smote_nb.score(test_txt, y_test))

	cal_auc()

	return tfidf_smote_nb, tfidf_smote_nb.predict_log_proba(test_txt)