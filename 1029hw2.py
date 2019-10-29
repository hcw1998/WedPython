# coding: utf-8
import sympy as sp
from sympy.abc import x,y
f = x**3*y + y**2 + x + y +15
f
ANS = sp.integrate(f,(x,1,5),(y,1,5))
ANS
practice = input(">>")
trans = str(ANS)
if(trans == practice):
    print("correct")
else:
    print("wrong")
