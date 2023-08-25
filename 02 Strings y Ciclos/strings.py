country='Colombia'

print(country[0])
print(country[1])

print(len(country))

second_letter=country[1]
print(id(second_letter))

other_var='o'
print(id(other_var))

print(id('C'))
#Agrega un espacio en la cadena
country += 'S'
print((country))
print(id(country))

platzi='platzi'

print(platzi.upper()) #Letras en mayusculas
print(platzi.startswith('p')) #Bool si inicia con la letra
print(platzi.find('la'))
print(dir(platzi))

def my_function():
    '''Este es un texto de ayuda'''
help(my_function)