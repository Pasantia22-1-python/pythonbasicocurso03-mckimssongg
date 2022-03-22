import sys

clientes = ['pablo', 'alguien']
def crearCliente(ClienteName):
    global clientes
    if ClienteName not in clientes:
        clientes.append(ClienteName)
    else: print( "Cliente ya esta agregado")

def buscarCliente(nameCliente):
    global clientes
    for i in clientes:
        if i != nameCliente:
            continue
        else: return True

def listaClientes():
    global clientes
    for i, cliente in enumerate(clientes):
        print(f"{i}: {cliente}")

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
        clientes.remove(nameCliente)
    else: print("este cliente no existe")


def _print_welcome():
    print('Bienvenido')
    print('*' * 30)
    print("""
    [C] para crear un nuevo cliente
    [L] para ver lista de clientes
    [U] para actualizar datos del cliente
    [D] para eliminar clientes
    [S] para buscar cliente
    """)


    
if __name__ ==  "__main__":
    _print_welcome()
    comando = input("Que deseas hacer ahora? ")
    comando = comando.upper()
    if comando == "C":
        listaClientes()
        name = getNameCliete()
        crearCliente(name)
        listaClientes()
    elif comando == "L":
        listaClientes()
    elif comando == "U":
        name = getNameCliete()
        newName = input("nuevo nombre del cliente  ")
        up_Cliete(name, newName)
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
        print("Opcion aun no disponible")