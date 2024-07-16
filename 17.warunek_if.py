# -*- coding: utf-8 -*-
# %%
lajki = 600
udostepnienia = 60

# %%
if lajki >= 500 and udostepnienia >= 100:
    print('Ceny spadaja o 10%')
else:
    print('Za mało lajkow lub udostepnien')

# %%
isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False

# %%
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Dziekujemy. Dostajesz kupon na burgera')
else:
    print('Zachecamy do dalszych zakupow')
    
# %%
diskSize = 160
diskSizeUsed = 133
fileSize = 10

# %%
if diskSize - diskSizeUsed >= fileSize:
    print('Mozna instalowac ')
else:
    print('Za mało miejsca na dysku')