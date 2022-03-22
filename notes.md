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