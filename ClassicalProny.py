def prony(t, F):
    N = len(t)
    m = int((N + 1) / 2)
    Amat = np.zeros((N-m, m))
    bmat = F[m:N]

    for jcol in range(m):
        Amat[:, jcol] = F[m-jcol-1:N-1-jcol]
        
    sol,_,_,_ = np.linalg.lstsq(Amat, bmat, rcond = None)
    
    # Solve the roots of the polynomial 
    c = np.zeros(m + 1,dtype = 'complex_')
    c[m] = 1.
    for i in range(1, m + 1):
        c[m-i] = -sol[i-1]
    u = np.complex128(poly.polyroots(c))
    
    b_est = np.complex128(np.log(u)) 

    # Finding the mk
    Amat = np.zeros((N, m), dtype = 'complex_')
    bmat = F
    for irow in range(N):
        Amat[irow, :] = u**irow

    a_est,_,_,_ = np.linalg.lstsq(Amat, bmat, rcond = None)

    return a_est, b_est