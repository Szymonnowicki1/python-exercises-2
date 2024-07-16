# -*- coding: utf-8 -*-
"""Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10"""

# %%
file_path = r'c:\temp\data_input\orders.csv' 

# %%
with open(file_path, 'r') as file:
    for line in file:
        line.replace('\n', '')
        order = line.split(',')
        
        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s')
        else:
            print("Line %s malformed!!!", line)
        
print('koniec')

