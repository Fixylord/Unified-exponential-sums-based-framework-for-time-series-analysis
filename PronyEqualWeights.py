def func_prony_abs(l, g, M, K):
    mu = g[0]
    res = 0
    for m in range(1,M):
        l_sum = 0
        for k in range(K):
            l_sum += (l[2*k]+1j*l[2*k+1]) ** m
        res += np.square(abs(g[m] - mu*l_sum/K))
    return res

def prony_equal(g, M, K, method)
    x0 = [0.0]*2*K
    res = sc.minimize(func_prony, x0, args=(g), method=method, jac=None, tol=None, callback=None, options={'gtol': 1e-5, 'maxiter': None, 'disp': False, 'return_all': False})
    lamb_eq = []
    for k in range(0, 2 * K, 2):
        lamb_eq.append(complex(res.x[k], res.x[k+1]))
    return lamb_eq

def prony_restoration(g, M, K, lamb_eq)
    g_eq = []
    mu = g[0]
    for m in range(1, M):
        l_sum = 0
        for k in range(K):
            l_sum += lamb_eq[k] ** m
        g_eq[m] = mu * l_sum / K
    return g_eq