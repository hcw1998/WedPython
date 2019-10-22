# coding: utf-8
from ipywidgets import interact
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
def draw(x):
    for i in range(x):
        s = "*" * (2*i + 1)
        print(f"{s:^51s}")
interact(draw, x = (0,20))
