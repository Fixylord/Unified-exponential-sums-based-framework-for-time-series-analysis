def generate_values_rand(n, k):
    t = np.arange(0, n, 1)
    s = np.zeros(n)
    mk = np.zeros(n)
    lambk = np.zeros(n)
    for t_n in t:
        mk[t_n] = np.random.uniform(1, 5)
        lambk[t_n] = np.random.uniform(0.0001, 0.1)
        s[t_n] = mk[t_n] * (np.exp(lambk[t_n] * t_n)) + k
    return t, s

def generate_data_real_prices(timeSeries):
    data = pd.read_csv(timeSeries)[::-1]
    close_price = data.ix[:, 'Adj Close'].tolist()
    close_price = close_price[:10]
    n = len(close_price)
    s = close_price
    t = np.arange(0, n, 1)
    return t, s, n

def generate_values_def(n, k):
    t = np.arange(0, n, 1)
    s = np.zeros(n)
    for t_n in t:
        s[t_n] = np.sin(t_n) + t_n + k
        #s[t_n] = t_n + k
        #s[t_n] = np.sin(t_n) + k
    return t, s