#No podemos modificar las tuplas, son inmutables
a=1,2,3
print(type(a))

a=(1,2,3)
print(type(a))
print((a[0]))
print((a[1]))
a=(1,1,1,2,3)

print(dir(a))
print(a.count(2))
print(a.count(1))
print(a.index(1))
print(a.index(3))

a=set([1,2,3])
b={3,4,5}

#Los sets no pueden tener duplicados
a.add(20)
print(a)

print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(a.remove(20))
print(a)
print(dir(set))