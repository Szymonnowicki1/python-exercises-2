# -*- coding: utf-8 -*-
import os
filename = input('Podaj nazwe pliku z poprzedniego zadania :')
while not os.path.isfile(filename):
    print('Nie ma takiej scieżki!')
    
webaddresses = []
with open(filename, 'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
for line in webaddresses:
    if line.endswith('.pl'):
        print("adres {} jest adresem z Polski".format(line))
    else:
        print("adres {} nie jest adresem z Polski".format(line))