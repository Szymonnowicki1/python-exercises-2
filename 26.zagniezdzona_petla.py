# -*- coding: utf-8 -*-
# %%
i = 10
y = 1

for x in range(1, i + 10):
    y *= x
    
print(i, y)
    
# %%
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(adj, noun)
