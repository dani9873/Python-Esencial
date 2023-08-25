import random

lista_de_numeros=list(range(100))
print(lista_de_numeros)

pares=[numero for numero in lista_de_numeros if numero % 2 == 0]
print('\n',pares)

student_uid=[1,2,3]
students=['Juan','Jose','Larsen']
students_whit_uid={uid: student for uid, student in zip(student_uid,students)}
print(students_whit_uid)

random_numbers=[]
for i in range(10):
    random_numbers.append(random.randint(1,3))
print(random_numbers)

non_repeated={number for number in random_numbers}
print (non_repeated)
#Comprehensions = son constructores que nos permiten generar secuencias a partir de otras secuencias
#Set comprehension Dictionary comprehension List comprehension