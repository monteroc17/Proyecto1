__author__ = 'Daniel y Luis'

#
def crear():
    nombre=str(input("Digite el nombre para su archivo:"))
    print("Archivo Guardado Correctamente")
    archivo=open(nombre+".py","w")
    menu()
def compilar():
    print("en proceso")

def menu():
    print("BIENVENIDO AL SIMULADOR DE INTÉRPRETE ITALI-NOVIS")
    print("Por favor, escoja la opción que desee digitando su número correspondiente")
    print("1.Nuevo Archivo")
    print("2.Compilar")
    opcion=int(input("--"))
    if opcion==1:
        crear()
    elif opcion==2:
        compilar()

menu()