import sys
import os
import msvcrt
borrarPantalla = lambda: os.system ("cls")
borrarPantalla()
PausarPantalla = lambda: msvcrt.getch()


clientes = [
    {
        'nombre': 'Pablo',
        'compañia': 'Google',
        'email': 'correogenerico@gmail.com',
        'posicion':'software engineer',
    },
    {
        'nombre': 'Juan',
        'compañia': 'COCA',
        'email': 'correogenerico@gmail.com',
        'posicion':'Coca engineer',
    }
]

def crearCliente(Cliente):
    global clientes
    if Cliente not in clientes:
        clientes.append(Cliente)
    else: print( "Cliente ya esta agregado")

def camposCliente(camposCliente):
    campo = None
    while not campo:
        campo = input(f'Cual es {camposCliente} del cliente?  ')
    return campo

def buscarCliente(nameCliente):
    global clientes
    for i in clientes:
        if i != nameCliente:
            continue
        else: return True

def listaClientes():
    global clientes
    for i, cliente in enumerate(clientes):
        print(f"{i} | {cliente['nombre']} | {cliente['compañia']} | {cliente['email']} | {cliente['posicion']} | ")

def getNameCliete():
    name = None
    while not name:
        name = input("Cual es el nombre del cliente?:  ")
        if name == 'exit':
            name = None
            break
    if not name: sys.exit()
    return name

def up_Cliete(clienteName, newName):
    global clientes
    if clienteName in clientes:
        index = clientes.index(clienteName)
        clientes[index] = newName
    else: print("clietne no se encuentra")


def deleteCLiente(nameCliente):
    global clientes
    if cliente in clientes:
        clientes.remove(cliente[nameCliente])
    else: print("este cliente no existe")


def _print_welcome():
    borrarPantalla()
    print('     Bienvenido')
    print('*' * 30)
    print("""
    [C] para crear un nuevo cliente
    [L] para ver lista de clientes
    [U] para actualizar datos del cliente
    [D] para eliminar clientes
    [S] para buscar cliente
    [E]
    """)


end = False
while not(end):
    if __name__ ==  "__main__":
        _print_welcome()
        comando = input("Que deseas hacer ahora? ")
        comando = comando.upper()
        if comando == "C":
            cliente = {
                'nombre': camposCliente('nombre'),
                'compañia': camposCliente('compañia'),
                'email': camposCliente('email'),
                'posicion': camposCliente('posicion'),
            }
            crearCliente(cliente)
            listaClientes()
        elif comando == "L":
            listaClientes()
        elif comando == "U":
            name = getNameCliete()
            cliente = {
                'nombre': camposCliente('nombre'),
                'compañia': camposCliente('compañia'),
                'email': camposCliente('email'),
                'posicion': camposCliente('posicion'),
            }
            up_Cliete(name, cliente['nombre'])
            listaClientes()
        elif comando == "D":
            name = getNameCliete()
            deleteCLiente(name)
            listaClientes()
        elif comando == "S":
            name = getNameCliete()
            found = buscarCliente(name)
            if found:
                print(f"El cliente {name} esta en la lista")
            else: print(f"El cliente {name} NO esta en la lista")
        elif comando == 'E':
            end = True
            print("Goodbye!")
        else:
            print(f"la opcion {comando} no existe")
    PausarPantalla()
    borrarPantalla()