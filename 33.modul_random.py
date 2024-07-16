# -*- coding: utf-8 -*-
# %%
from random import *

# %%
min = 1
max = 6
dice = randint(min, max)

# %%

if dice == 1:
    print('o')
elif dice == 2:
    print('o o')
elif dice == 3:
    print('o o o')
elif dice == 4:
    print('o o')
    print('o o')
elif dice == 5:
    print('o o')
    print(' o')
    print('o o')
else:
    print('o o')
    print('o o')       
    print('o o')         
    
# %%
dices = []
for x in range(5):
    dices.append(randint(1, 6))
   
dices.sort()
print(dices)











