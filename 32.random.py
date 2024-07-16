# -*- coding: utf-8 -*-
# %%
from random import *

# %%
for x in range(1, 10):
    print(randint(1, 100))

# %%
number1 = randint(1, 100)
counter = 1
number2 = randint(1, 100)

# %%
while number1 != number2:
    counter += 1
    number2 = randint(1, 100)
    print(counter, number2)
    
# %%
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

# %%
shuffle(countries)
groupNumber = 0

# %%
for y in range(len(countries)):
     if y % 4 == 0:
         groupNumber += 1
         print('Grupa {}'.format(groupNumber))
     print(countries[y])
           
























