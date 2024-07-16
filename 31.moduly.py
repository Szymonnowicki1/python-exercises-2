# -*- coding: utf-8 -*-
# %%
percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]

# %%
print(percent.sort())

# %%
from statistics import *

# %%
median_low(percent)

# %%
median_high(percent)

# %%
median(percent)

# %%
import math

# %%
degree = 45
# 1 rad = 180°/π 

# %%
rad = degree * math.pi / 180
print(rad)

# %%
math.radians((45))

# %%
small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

# %%
 x = math.pi * small_pizza_r ** 2
print(x)
z = math.pi * big_pizza_r ** 2
print(z)
y = math.pi * family_pizza_r ** 2
print(y)



























