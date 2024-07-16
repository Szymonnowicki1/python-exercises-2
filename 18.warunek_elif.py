# -*- coding: utf-8 -*-
# %%
lajki = 600
udostepnienia = 60

# %%
if lajki < 500:
    print('Za mało lajkow')
elif udostepnienia < 100:
    print('Za mało udostepnien')
else:
    print('Ceny produktów obnizone o 10%')
    
# %%
isPizzaOrdered = False
isBigdrinkOrdered = False
isWeekend = True

# %%
if  isWeekend:
    print('Promocja dotyczy tylko w dni powszednie')
elif  not (isBigdrinkOrdered or isPizzaOrdered):
    print('Brakuje pizzy lub duzego napoju')
else:
    print('Burger za free')

































