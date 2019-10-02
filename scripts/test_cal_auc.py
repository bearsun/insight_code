import unittest
import numpy as np
import pandas as pd
from cal_auc import cal_auc
from sklearn.dummy import DummyClassifier

class TestAUCMethods(unittest.TestCase):

	def test_cal1(self):
		X_test = np.ones((500, 1000))
		np.random.seed(0)
		y_test = pd.Series(np.random.randint(31, size=500))
		clf = DummyClassifier(random_state = 0, strategy = 'constant', constant = 0)
		clf.fit(X_test, y_test)
		auc = round(cal_auc(clf, X_test, y_test), 2)
		self.assertEqual(auc, .51)

if __name__ == '__main__':
	unittest.main()
