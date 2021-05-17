def draw_time_series(t, s, n_min, n_max, title, label):
    plt.figure(figsize=(16, 10))
    plt.grid(True)
    plt.plot(t[n_min:n_max], s[n_min:n_max], 'o', label = label, markersize = 4)
    plt.plot(t[n_min:n_max], s[n_min:n_max])
    plt.legend(fontsize=18)
    plt.ylabel('S(t)', fontsize=18)
    plt.xlabel('t', fontsize=18)
    plt.title(title, fontsize=18)

def draw_s_value(t, series, col):
    plt.scatter(t - 1, series[t - 1], c = col, s = 100) 
    
def write_s_value(t, series, type_s):
    print(type_s, " s for t =", t - 1, "is", series[t - 1])