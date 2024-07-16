# -*- coding: utf-8 -*-

import os

import time

# %%
dir = input('wprowadz sciezke dostepu do katalogu :')

if not os.path.isdir(dir):
    print('musisz wprowadzic katalog {} :'.format(dir))
else:
    file = input('wprowadz nazwe pliku {} :'.format(dir))

    path = os.path.join(dir, file)

    if not os.path.isfile(path):
        print('nie istnieje taki plik {}'.format(path))
    else:
        print(dir, file)
        print(time.localtime(os.path.getmtime(path)))
        print(os.path.getsize(path))
        print(os.path.dirname(path))
        
# %%
os.getcwd()
