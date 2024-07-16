# -*- coding: utf-8 -*-
import os

import datetime

# %%
data_input_catalog = r'c:\temp\data_input'
data_output_catalog = r'c:\temp\data_output'
today = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
is_input_catalog_ok = os.path.isdir(data_input_catalog)
is_output_catalog_ok = os.path.isdir(data_output_catalog)
is_today_output_catalog_ok = not os.path.isdir(today_output_catalog) and not os.path.isfile(today_output_catalog)

# %%
if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok is True:
    print('Conditions met! We can continue!')
else:
    print('Prerequisites not met! Check the paths!')
    if is_input_catalog_ok is True and is_output_catalog_ok is True and is_today_output_catalog_ok is False:
        print('plik o nazwie odpowiadającej dzisiejszej dacie istnieje')
    if is_input_catalog_ok or is_output_catalog_ok is False and is_today_output_catalog_ok is True:
        print('brak katalogu wejściowego lub wyjściowego (lub obu  na raz)')
    if is_input_catalog_ok or is_output_catalog_ok is False and is_today_output_catalog_ok is False:
        print('brak katalogu wejściowego lub wyjściowego (lub obu  na raz) i plik o nazwie odpowiadającej dzisiejszej dacie istnieje')
    
