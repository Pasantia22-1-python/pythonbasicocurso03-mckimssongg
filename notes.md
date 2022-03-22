# Notas 
```python
name = "Hola"
name[0] = "Hola" # X 
```
Este tipo de asignacion no funciona en strings

```python
lista = ["a", "b", "c", "d", "e", "f", "g"]
lista[2] = "perl" # √
```
Pero si puede usarse en listas

___
___


**Copy de listas**
```python
>>> lista = ["a", "b", "c", "d", "e", "f", "g"]
>>> listaB = lista
>>> id(lista)
2338922178752
>>> id(listaB)
2338922178752
>>> lista[0] = "peras"
>>> listaB
['peras', 'b', 'c', 'd', 'e', 'f', 'g']          # X 
```
Esta no es la forma correcta de hacer copy a una lista al menos que queramos que
mantenga el mismo espacio de memoria que la anterior, lo que provocara que al hacerle cambios al original, 
los tendra tambien la copia

```python
>>> import copy
>>> ListaB = copy.copy(lista)
>>> lista
['peras', 'b', 'c', 'd', 'e', 'f', 'g']
>>> lista[0] = "a"
>>> ListaB
['peras', 'b', 'c', 'd', 'e', 'f', 'g']
>>> id(ListaB)
2338922585152     # √
```

Lar forma correcta es importando copy y usando copy para copiar la lista

___
___


**Metodos de listas**
```python
>>> a = [1]
>>> a.append(3)
>>> a
[1, 3]
>>> #sacar el ultimo elemento
>>> b = a.pop()
>>> b
3
>>> a
[1]
```

**Eliminar elementos de una listas**

```python
>>> a
[1, 3, 5, 6]
>>> a.remove(3)
>>> a
[1, 5, 6]
>>> del a[-1]
>>> a
[1, 5]
```

**operadores con listas**
```python
>>> a
[1, 5]
>>> a
[1, 5]
>>> a * 3
[1, 5, 1, 5, 1, 5]
>>> a + lista
[1, 5, 'a', 'b', 'c', 'd', 'e', 'f', 'g']
```
___
___

**Diccionarios**

```python
>>> comida = {}
>>> comida['pizza'] = "Pizza bambino"
>>> comida.keys()
dict_keys(['pizza'])
>>> comida.values()
dict_values(['Pizza bambino'])
>>>
```
___
___

**Tuplas**

Son inmutables
```python
>>> a = (1,2,3,4)
>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> a.count(3)
1
>>> a.index(3)
2
>>>
```
___
___


**Conjuntos**

-Sus elementos no se pueden repetir

```python
>>> a = set([1,2,3])
>>> b = {3,4,5}
>>> type (a)
<class 'set'>
>>> type (b)
<class 'set'>
>>> a.add(3)
>>> a
{1, 2, 3}
>>> a.add(20)
>>> a
{1, 2, 3, 20}
>>> a.intersection(b)
{3}
>>> a.union(b)
{1, 2, 3, 20, 4, 5}
>>> b.difference(a)
{4, 5}
>>>
```

___
___

**Comprehensions**

```python
>>> students_uid = [1,2,3]
>>> students = ["Felipe", "Giselle","Kruaka"]
>>> students_with_uid = {uid: student for uid, student in zip(students_uid, students)}
>>> students_with_uid
{1: 'Felipe', 2: 'Giselle', 3: 'Kruaka'}
```