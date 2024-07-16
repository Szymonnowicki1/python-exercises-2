# -*- coding: utf-8 -*-
# %%
def ilednidokonca():
    from datetime import date
    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
    
ilednidokonca()

# %%
def PrintAnimal(*animals):
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
    
    
    for animal in animals:
        
        if animal == 'cat':
            print(txt_cat)
        elif animal == 'bear':
            print(txt_bear)
        elif animal == 'bat':
            print(txt_bat)
        else:
            print('Błąd')
        
    

   
    
# %%
PrintAnimal('cat', 'bat', 'horse')

# %%
from datetime import date
def DaysToEndOfYear(*wieledat):
    
    for date_today in wieledat:
        
        date_end_year = date(2021, 12, 31)
        delta = date_end_year - date_today
        print('dzisiejsza data:', date_today, 'do konca roku jest :', delta)
    
# %%
print('dzien 1 grudnia 2020 do konca roku zostało:', DaysToEndOfYear(2020, 12, 1), 'dni')

# %%
DaysToEndOfYear(date(2021, 12, 1))

























