# reference - https://www.geeksforgeeks.org/multiclass-classification-using-scikit-learn/

def DecisionTreeClassifier_Model(X_train,y_train,X_test):
    from sklearn.tree import DecisionTreeClassifier
    dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train)
    y_predict = dtree_model.predict(X_test)
    return y_predict, dtree_model

def SVC_Model(X_train,y_train,X_test):
    from sklearn.svm import SVC
    svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
    y_predict = svm_model_linear.predict(X_test)
    return y_predict, svm_model_linear

# KNN (k-nearest neighbours) classifier
def KNeighborsClassifier_Model(X_train,y_train,X_test) :
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier().fit(X_train, y_train)
    y_predict = knn.predict(X_test)
    return y_predict, knn

# Naive Bayes classifier
def GaussianNB_model(X_train,y_train,X_test) :
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB().fit(X_train, y_train)
    y_predict = gnb.predict(X_test)
    return y_predict, gnb

# reference - https://medium.com/@b.terryjack/tips-and-tricks-for-multi-class-classification-c184ae1c8ffc
def RandomForestClassifier_model(X_train,y_train,X_test) :
    from sklearn.ensemble import RandomForestClassifier
    rf_classifier = RandomForestClassifier()
    rf_classifier.fit(X_train, y_train)
    y_predict = rf_classifier.predict(X_test)
    return y_predict, rf_classifier

def MLPClassifier_model(X_train,y_train,X_test):
    from sklearn.neural_network import MLPClassifier
    snn_classifier = MLPClassifier()
    snn_classifier.fit(X_train, y_train)
    y_predict = snn_classifier.predict(X_test)
    return y_predict, snn_classifier

def lightgbm_model(train, valid, test, target, param = None, num_round = 1000, early_stopping_rounds = 10):
    import lightgbm as lgb

    if param is None:
        param = {'num_leaves': 64, 'objective': 'binary', 'metric':'auc'}

    feature_cols = train.columns.drop(target)
    dtrain = lgb.Dataset(train[feature_cols], label=train[target])
    dvalid = lgb.Dataset(train[feature_cols], label=train[target])

    bst = lgb.train(param, dtrain, num_round, valid_sets=[dvalid], early_stopping_rounds = early_stopping_rounds)
    y_predict = bst.predict(test[feature_cols])
    return y_predict, bst
