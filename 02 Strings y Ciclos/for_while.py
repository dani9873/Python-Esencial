#Para itera a lo largo de una secuencia
print(range(10))

for i in range(10):
    print(i)

 #Para itera mientras que se cumpla una condicion

def cuenta_regresiva(n):
    while n > 0:
        print(n)
        n-=1
cuenta_regresiva(10)

#ciclo infinito
'''def cuenta_regresiva(n):
    while n > 0:
        print(n)
        n+=1
cuenta_regresiva(10)'''