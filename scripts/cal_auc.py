from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import roc_curve, auc

def cal_auc(model, X_test, y_test):
	'''
	calculate micro auc across all classes

	input
	-----
	obj model: model file with function predict_proba
	pd.df X_test: testing data features
	pd.df y_test: testing data labels

	output
	-----
	None
	'''

	# prediction probability
	y_test_prob = model.predict_proba(X_test)

	# one-hot encode 31 classes
	enc = OneHotEncoder()
	y_test_ohe = enc.fit_transform(y_test.values.reshape(-1, 1)).toarray()

	# Compute ROC curve and ROC area for each class
	n_classes = 31
	fpr = dict()
	tpr = dict()
	roc_auc = dict()
	for i in range(n_classes):
	    fpr[i], tpr[i], _ = roc_curve(y_test_ohe[:, i], y_test_prob[:, i])
	    roc_auc[i] = auc(fpr[i], tpr[i])

	# calculate micro auc
	fpr["micro"], tpr["micro"], _ = roc_curve(y_test_ohe.ravel(), y_test_prob.ravel())
	roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

	print('auc:')
	print(roc_auc['micro'])

#	return roc_auc['micro']