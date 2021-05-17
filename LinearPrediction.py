def create_dataset(n, t, s):
    s_add_full = s
    for t_add in range(n - 1):
        s_add = np.zeros(n)
        s_add[t_add+1:] = s[t_add]
        s_add_full = np.vstack((s_add_full, s_add))
    
    s_dataset = (np.vstack((s_add_full, t))).transpose()

    dataset_s = pd.DataFrame(s_dataset.reshape(n,n+1))
    dataset_s = dataset_s.fillna(method='ffill')
    return dataset_s

def split_dataset(dataset_s, n):
    f = np.arange(1,n+1,1)

    test_set = dataset_s[n-1:].values
    Y_test = np.array(test_set[0][0])
    X_test = np.array(test_set[0][1:])
    X_test = np.array(X_test).reshape(1, -1)

    dataset_s = dataset_s.drop(np.where(dataset_s[n] == n - 1)[0])

    Y = dataset_s[0].values
    X = dataset_s[f].values
    return X, X_test, Y, Y_test

def LP_predict(X, X_test, Y, s, n):
    regressor = LinearRegression()  
    regressor.fit(X, Y)
    Y_pred = regressor.predict(X_test)
    s_for_predict = np.delete(s, n - 1)
    s_predict = np.append(s_for_predict, Y_pred)
    return s_predict
    