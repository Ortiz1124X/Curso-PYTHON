
year = 0

def es_bisiesto(year):
    return not year % 4 and (year % 100 or not year % 400)


for year in range(1600, 1800):
    if es_bisiesto(year):
        print(year, end=' ')

        continue

from calendar import isleap

for annio in range(1800, 2022):
    if isleap(annio):
        print(annio, end=' ')
