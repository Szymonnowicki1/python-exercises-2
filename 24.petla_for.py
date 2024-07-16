# -*- coding: utf-8 -*-
# %%
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for lista in data:
    print(lista.upper())
    
# %%
for x in data:
    elements = x.split(':')
    
    if 'Error' in elements[0]:
        print(elements[1].upper())
    else:
        print(elements[1])
        
# %%
for s in data:
 
    elements = s.split(':')
    if elements[0] == 'Error':
        print(elements[1].upper())
    else:
        print(elements[1])
        

