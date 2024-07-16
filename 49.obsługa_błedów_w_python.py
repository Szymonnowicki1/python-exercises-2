# -*- coding: utf-8 -*-
import os

line = (input('Jaka jest akceptowalna cena nastepnego kursu na Udemy :'))
filepath = input('sciezka do pliku :')
try:
    value = int(line)
    file = open(filepath, 'w+')
    file.write(line)
    file.close()
except FileNotFoundErroras as e:
    print("Error opening file", filepath, e)
except ValueError as e:
    print("The value entered cannot be converted to a number")
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
else:
    print("Actions completed successfully")

