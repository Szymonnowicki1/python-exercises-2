# -*- coding: utf-8 -*-
import sys
file_path = r'C:\Users\szymu\OneDrive\Pulpit\kurs2\orders.csv'
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore {}, item {}, amount {}'.format(pharmacy_name, item, amount))
        except IndexError as e:
            print('doszło do błędu związanego z brakiem dostatecznej ilośći pól. problem z linia %s' % line)
        except ValueError as e:
            print('doszło do błędu związanego z niepoprawną konwersją danych w trzecim polu do typu int. problem z linia %s' % line)
        except:
            print("Problem %s" % sys.exc_info())
            
            
print("Processing finished")
                  