from sklearn.feature_extraction.text import CountVectorizer
from imblearn.over_sampling import SMOTE
from sklearn.naive_bayes import MultinomialNB
from cal_auc import cal_auc

def model3(X_train, X_test, y_train, y_test):
	'''
	model2: entity data + textrank keywords extraction + bag-of-words + SMOTE + multinomialNB

	input
	-----
	pd.df X_train: training text
	pd.df X_test: testing text
	pd.df y_train: training labels
	pd.df y_test: testing labels

	output
	-----
	np.array log_proba: log probability of prediction
	'''


	# get keywords from textrank
	f = open('txt_kwords.txt','r')
	kwords = f.read()
	f.close()

	vocabulary = kwords.split('@')

	# tf-idf
	vectorizer = CountVectorizer(vocabulary=vocabulary[:3000])
	train_txt = vectorizer.fit_transform(X_train['entity'])
	test_txt = vectorizer.transform(X_test['entity'])

	# SMOTE
	X_train_resampled, y_train_resampled = SMOTE(random_state=0).fit_resample(train_txt, y_train)

	# Multinomial Naive Bayes
	ent_txtrk_smote_nb = MultinomialNB()
	ent_txtrk_smote_nb.fit(X_train_resampled, y_train_resampled)

	# prediction
	print('TextRank model')
	print('training acc:')
	print(ent_txtrk_smote_nb.score(train_txt, y_train))

	print('testing acc:')
	print(ent_txtrk_smote_nb.score(test_txt, y_test))

	cal_auc()

	return ent_txtrk_smote_nb.predict_log_proba(test_txt)