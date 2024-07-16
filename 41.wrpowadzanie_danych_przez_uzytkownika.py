# -*- coding: utf-8 -*-
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

# %%
import math

# %%
a_str = input('podaj wspolczynnik a:')
b_str = input('podaj wspolczynnik b:')
c_str = input('podaj wspolczynnik c:')


if not( check_int(a_str) and check_int(b_str) and check_int(c_str) ):
    print('a, b i c musi byc int')
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)

    if a == 0:
        print('to nie jest rownianie kwadratowe')
    else:
        delta = b ** 2 - (4 * a * c)
            
        if delta < 0:
            print('brak rozwiazan')
        elif delta == 0:
            x1 = - b / (2 * a)
            print('x1 =', x1)
        else:
            x1 = (-b-delta**0.5)/(2*a)
            x2 = (-b+delta**0.5)/(2*a)
            print('x1 =', x1)
            print('x2 =', x2)
            
        
    
        
          
    
    

            
            
            
            
            
            
            
            
            
            