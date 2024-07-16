# -*- coding: utf-8 -*-
# %%
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for x in range(10):
    print(string_A)

# %%
for y in range(1, 10):
    if y % 2 == 0:
        print(string_B)
    else:
        print(string_A)
        
# %%
for z in range(10):
    print(z * 'x')
    
# %%
for c in range(10):
    if c % 2 == 0:
        print(c * 'x')
    else:
        print(c * 'o')
   
