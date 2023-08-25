#Las listas son mutables
import copy 

countries=['Mexico','Venezuela','Colombia','Argentina','Guatemala']
print(id(countries))
print(countries)

ages=[12,18,24,34, 50]
print(id(ages))

receta=['Ensalada',2,'lechugas',5,'jitomates']

countries[0]='España'
print(countries)

#alias
global_countries=countries
global_countries_copi=copy.copy(countries)
print(global_countries)

countries[0]='Guatemala'

print(countries)
print(global_countries)
print(global_countries_copi)

for country in countries:
    print(country)