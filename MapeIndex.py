def MAPE_extra(s_orig, s_pred):
    MAPE = abs((s_orig - s_pred) / s_orig) * 100
    print("MAPE index:", MAPE, "%")
    
def MAPE_int(s_orig, s_pred):
    sum_s = 0
    for i in range(1, len(s_orig)):
        
        sum_s += abs((s_orig[i] - np.real(s_pred[i])) / s_orig[i]) 
        
    MAPE = (sum_s / len(s_orig)) * 100 
    print("MAPE index:", MAPE, "%")