# -*- coding: utf-8 -*-
# %%
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

x = 0
y = len(numbers) - 2

# %%
while x <= y:
    print('liczba :', x, numbers[x], numbers[x+1])
    if numbers[x] ** 2 == numbers[x + 1]:
        print('\TFOUND')
    x += 1
    
# %%
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

x = 0
y = len(numbers) - 3

# %%
while x <= y:
    print(x, numbers[x], numbers[x + 1], numbers[x + 2])
    if numbers[x] ** 2 == numbers[x + 1] and numbers[x + 1] ** 2 == numbers[x + 2]:
        print('\FOUND')
    x += 1
    
# %%
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

x = 0
y = len(texts) - 2

# %%
while x <= y:
    print(x, texts[x], texts[x + 1])
    if len(texts[x]) == len(texts[x + 1]):
        print('\FOUND')
    x += 1
    
    
    
    