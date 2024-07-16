# -*- coding: utf-8 -*-
# Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
# Zakladamy ze:
# -liczba mrugniec na minute to 20
# -liczba minut w godzinie to 60
# -liczba godzin w dobie 24
# -liczba lat (czyli nasz X) 50
# Uwaga: jezeli przyjac ze spimy 8 godzin to liczba godzin na dobe
# powinna wynosic 16


# liczba mrugniec  okiem na minute
blinksPerMin = 20

# liczba minut na godzine i liczba godzin w dobie 
minInHour = 60
hoursInDay = 24
daysInYear = 365

# liczab lat
years = 50

# liczba mrugniec w ciagu X lat 
print(20 * 60 * 16 * 50 * 365)
