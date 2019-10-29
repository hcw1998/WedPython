# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
π = np.pi
x = np.linspace(-2*π, 1*π, 500)
y = np.sin(x)
plt.plot(x,y,)
plt.scatter(x[y>0], y[y>0])
plt.scatter(x[y<-0.5], y[y<-0.5], c='#FF235A')
