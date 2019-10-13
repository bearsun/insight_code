from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import roc_auc_score


def cal_auc(model, X_test, y_test, method = 'micro'):
    '''
    calculate micro auc across all classes

    input
    -----
    obj model: model with function predict_proba
    pd.df X_test: testing data features
    pd.df y_test: testing data labels
    str method: the method to average across classes

    output
    -----
    float: micro auc
    '''

    # prediction probability
    prob = model.predict_proba(X_test)

    # binarize 31 classes
    lb = LabelBinarizer()
    true = lb.fit_transform(y_test)

    return roc_auc_score(true, prob, average = method)
