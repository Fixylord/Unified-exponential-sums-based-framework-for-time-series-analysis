def isscalar(x):
    #Returns true if x is scalar value
    return not isinstance(x, (list, tuple, dict, np.ndarray))

def nans(dims):
    return np.nan * np.ones(dims)

def ssa(y, dim) -> tuple:
    n = len(y)
    t = n - (dim - 1)

    yy = linalg.hankel(y, np.zeros(dim))
    yy = yy[:-dim + 1, :] / np.sqrt(t)

    _, s, v = linalg.svd(yy, full_matrices=False, lapack_driver='gesvd')

    vt = np.matrix(v).T
    pc = np.matrix(yy) * vt

    return np.asarray(pc), s, np.asarray(vt)

def inv_ssa(pc: np.ndarray, v: np.ndarray, k) -> np.ndarray:
    if isscalar(k): k = [k]

    if pc.ndim != 2:
        raise ValueError('pc must be a 2-dimensional matrix')

    if v.ndim != 2:
        raise ValueError('v must be a 2-dimensional matrix')

    t, dim = pc.shape
    n_points = t + (dim - 1)

    if any(filter(lambda x: dim < x or x < 0, k)):
        raise ValueError('k must be vector of indexes from range 0..%d' % dim)

    pc_comp = np.asarray(np.matrix(pc[:, k]) * np.matrix(v[:, k]).T)

    xr = np.zeros(n_points)
    times = np.zeros(n_points)

    # reconstruction loop
    for i in range(dim):
        xr[i : t + i] = xr[i : t + i] + pc_comp[:, i]
        times[i : t + i] = times[i : t + i] + 1

    xr = (xr / times) * np.sqrt(t)
    return xr

def ssa_predict(x, dim, k, n_forecast, e=None, max_iter=10000) -> np.ndarray:
    if not e:
        e = 0.0001 * (np.max(x) - np.min(x))
    mean_x = x.mean()
    x = x - mean_x
    xf = nans(n_forecast)

    for i in range(n_forecast):
       
        x = np.append(x, x[-1])
        yq = x[-1]
        y = yq + 2 * e
        n_iter = max_iter
        while abs(y - yq) > e:
            yq = x[-1]

            pc, _, v = ssa(x, dim)
            xr = inv_ssa(pc, v, k)

            y = xr[-1]
            x[-1] = y
            n_iter -= 1
            if n_iter <= 0:
                print('ssa_predict> number of iterations exceeded')
                break

        xf[i] = x[-1]
    xf = xf + mean_x
    return xf

def ssa_forecast(n, s):
    s_for_predict = np.delete(s, n - 1)
    L = int(0.4 * n)

    s_forecast_ssa = ssa_predict(s_for_predict, L, [0], 10, 0.1)

    s_predict = np.append(s_for_predict, s_forecast_ssa)
    return s_predict