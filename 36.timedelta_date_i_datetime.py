# -*- coding: utf-8 -*-
# %%
from math import *

# %%
inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

# %%
len(inputdata)
len(factortable)

# %%
if len(inputdata) == len(factortable):
    print('OK')
elif len(inputdata) != len(factortable):
    print("inputdata and factortable need to have equal number of elements")
    
# %%
from datetime import *

# %%
datetime.today()

# %%
datetime.today().strftime("%Y-%m-%d")