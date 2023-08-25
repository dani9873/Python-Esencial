import random

a=list(range(0,100,2)) #Lista de numero pares
b=list(range(0,10))

print(a+b)
print(b*2)

#Es lo mismo que fruits=[] lista vacia
fruits=list()

#Añadir un elemento al final de la lista con append
fruits.append('apple')
print(fruits)
print(len(fruits))

fruits.append('banana')
print(fruits)
print(len(fruits))

fruits.append('kiwi')
print(fruits)
print(len(fruits))

#Eliminar el ultimo elemento de la lista utilizar pop, del, remove.
some_fruit=fruits.pop()
print(some_fruit)
print(fruits)

some_fruit=fruits.pop(0)
print(some_fruit)
print(fruits)

del fruits[0]
print(fruits)

random_numbers=[]

for i in range(10):
    random_numbers.append(random.randint(0,15))
print(random_numbers)

#Ordenar una lista de mayor a menor utilizar sort
#ramdom_numbers.sort()
order_numbers=sorted(random_numbers)
print(order_numbers)

order_numbers = random_numbers.sort()
print(order_numbers)
print(dir(random_numbers))