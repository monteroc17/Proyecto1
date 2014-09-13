__author__ = 'Daniel y Luis'

#
def crear():#Crear un nuevo archivo de python
    nombre=str(input("Digite el nombre para su archivo:"))#input para mque el usuario introduzca el nombre de su archivo
    print("Archivo Guardado Correctamente")
    archivo=open(nombre+".py","w")#Crea un archivo de python donde se guardará el codigo del usuario
    menu2(archivo)
    return archivo#se retorna para que el archivo sea utilizado en la función compilar

def compilar(archivo):#recibe como parametro el archivo .py crreado anteriormnte
    #lista con las palabras reservadas de python
    comandos_originales=["  ","\n","(",")","'","if","else","elif","and","def","del","is","from","not","or","try","in","as","for","return","break","while","import","print","input","int","str","float"]

    #lista con las palabras del nuevo codigo
    comandos_nuevos=["►",";","♪","♫","☼","se","altro","setro","con","definire","cance","un","da","non","oppure","provare","dentro","come","per","ritorno","pausa","mentre","importare","stampa","ingresso","intero","stri","flultuare"]
    contador=0
    while contador==0:
        codigo=str(input("Digite aquí su codigo:"))
        if codigo=="compilar":
            contador=1
            print("Su codigo se ha guardado exitosamente!")
        else:
            archivo.write(codigo+"\n")


    print("en proceso")

def menu2(archivo):
    print("Por favor, escoja la opción que desee digitando su número correspondiente")
    print("1.Nuevo Archivo")
    print("2.Compilar")
    opcion=int(input(">>"))#Input para que el usuario elija la opcion del menu que desee
    if opcion==1:
        crear()#Aquí se llama a la funcion "crear"
    elif opcion==2:
        compilar(archivo)#Aquí se llama a la funcion "compilar"

def menu():
    print("BIENVENIDO AL SIMULADOR DE INTÉRPRETE ITALI-NOVIS")
    print("Por favor, escoja la opción que desee digitando su número correspondiente")
    print("1.Nuevo Archivo")
    print("2.Compilar")
    opcion=int(input(">>"))#Input para que el usuario elija la opcion del menu que desee
    if opcion==1:
        crear()#Aquí se llama a la funcion "crear"
    elif opcion==2:
        compilar()#Aquí se llama a la funcion "compilar"

menu()