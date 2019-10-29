# coding: utf-8
f_1 = (-100*y**2 + 6*y -10)
f_2 = (100*y**2 - 7*y +2)
sp.plot(f_1, f_2)
for i in np.linspace(-10,10,100):
    count = (-100*i**2+6*i-10) - (100*i**4-7*i+2)/10
    plt.scatter(i, -count)
