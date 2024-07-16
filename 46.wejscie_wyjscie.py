# -*- coding: utf-8 -*-
import os

webaddresses = []

line = input('Podaj strone www :')

while line != '':
    webaddresses.append(line)
    line = input('Podaj strone www :')

print(webaddresses)
dirname = os.getcwd()
filename = input('Wprowadz nazwe pliku :')
filepath = os.path.join(dirname, filename)
file = open(filepath, 'w+')
for webaddress in webaddresses:
    
    file.write(webaddress+"\n")
file.close()

