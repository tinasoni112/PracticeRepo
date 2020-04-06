from PracticeRepo.MachineLearning.EDA.BasicEDA import *

def label_encoding(data,col):
    from sklearn.preprocessing import LabelEncoder
    labelencoder = LabelEncoder()
    encoded_data = labelencoder.fit_transform(data.loc[:,col])
    return encoded_data

def dummy_variables_one_hot_encode(data,col):
    from sklearn.preprocessing import OneHotEncoder
    import pandas as pd
    onehotencoder = OneHotEncoder(handle_unknown='ignore')
    encoded_data = onehotencoder.fit_transform(data[[col]])
    return encoded_data

def ordinal_encoding(data,col, order_cat):
    from sklearn.preprocessing import OrdinalEncoder
    ordinalencoder = OrdinalEncoder(categories=[order_cat])
    encoded = ordinalencoder.fit_transform(data[[col]].values.reshape(-1,1))
    encoded_data = flatten_list_of_list(encoded.tolist())
    return encoded_data

def sklearn_linear_model(X,y):
    from sklearn import linear_model
    lm = linear_model.LinearRegression()
    model = lm.fit(X, y)
    return model


def sklearn_train_test_split(X,y,test_size=0.2):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    return X_train, X_test, y_train, y_test

def pca_sklearn (data,n_components=None):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(data)
    return pca_data

def kMeans_sklearn (data,n_clusters, init):
    from sklearn.cluster import KMeans
    # Explicit initial center position passed: so only one init in k-means instead of n_init=10
    kMeans = KMeans(n_clusters=n_clusters, init=init, n_init=1)
    kMeans = kMeans.fit(data)
    return kMeans

def calc_purity_cluster(y_actual, y_predict):
    import numpy as np
    from sklearn.metrics.cluster import contingency_matrix

    contingency_matrix = contingency_matrix(y_actual, y_predict)
    return np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix)


def imputer_sklearn(data, cols):
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer()
    return imputer.fit_transform(data.loc[:,cols])

def scaler_sklearn(data):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    return scaler.fit_transform(data)

def polynomial_features_sklearn(data, n_degree = 2):
    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures(degree = n_degree)
    return poly_reg.fit_transform(data)
