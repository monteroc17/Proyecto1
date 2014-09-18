__author__ = 'Daniel y Luis'

#
def crear():#Crear un nuevo archivo de python
    nombre=str(input("Digite el nombre para su archivo:"))#input para mque el usuario introduzca el nombre de su archivo
    print("Archivo Guardado Correctamente")
    archivo=open(nombre+".py","w")#Crea un archivo de python donde se guardará el codigo del usuario
    menu2(archivo)
    return archivo#se retorna para que el archivo sea utilizado en la función compilar

def compilar(archivo):#recibe como parametro el archivo .py crreado anteriormnte
    print("Digite su codigo aqui")
    print("la palabra para terminar de escribir el codigo es 'compilar'")
    #lista con las palabras reservadas de python
    comandos_originales=["#""():","()",":","   ","(",")","'","if","else","elif","and","def","del","is","from","not","or","try","in","as","for","return","break","while","import","print(","print('","input(","input('","int(","int('","int","str(","str('","str","float(","float('","float","')","'))","')))"]
    #lista con las palabras del nuevo codigo
    comandos_nuevos=["@","♪♫^","♪♫","^","_","♪","♫",";","se","altro","setro","con","definire","cance","un","da","non","oppure","provare","dentro","come","per","ritorno","pausa","mentre","importare","stampa♪","stampa♪;","ingresso♪","ingresso♪;","intero♪","intero♪;","intero","stri♪","stri♪;","stri","flultuare♪","flultuare♪;","flutuare",";♫",";♫♫",";♫♫♫"]
    comandos=dict(zip(comandos_nuevos,comandos_originales))#convierte las 2 listas en un diccionario


    contador=0

    while contador==0:#el contador sirve para llevar un control de cuando el usuario quiera parar de introducir codigo
        codigo=str(input(">>"))#Input en el cual el usuario escribe 1 línea de código
        if codigo=="compilar":#Si el usuario digita "compilar" el contador cambia y el ciclo para
            contador=1
            print("Su codigo se ha guardado exitosamente!")
        elif codigo!="compilar":#Si el código es cualquier cosa menos compilar continua con el ciclo
            x=codigo.split()#Se almacena todo lo digitado en una lista
            for i in x:#ciclo que recorre toda la lista
                lista=[]#lista vacia cada vez que el ciclo comience
                if i in comandos:#si i está en el diccionario, agrega su equivalente (palabra reservada de python)
                    lista.append(comandos[i])
                else:#si el valor evaluado no está en el diccionario, simplemente lo agrega a la lista
                    lista.append(i)
                codigo_final=" ".join(lista)#De la lista final convierte todo en un string de los valores
                archivo.write(codigo_final+" ")#Aquí escribe en el archivo python el string final
            archivo.write("\n")#escribe un ENTER para que pase a escribir a la línea siguiente


def menu2(archivo):
    try:#Aquí se validan errores para menu2
        print("Por favor, escoja la opción que desee digitando su número correspondiente")
        print("1.Nuevo Archivo")
        print("2.Compilar")
        opcion=int(input(">>"))#Input para que el usuario elija la opcion del menu que desee
        if opcion==1:
            crear()#Aquí se llama a la funcion "crear"
        elif opcion==2:
            compilar(archivo)#Aquí se llama a la funcion "compilar"
        else:
            print("FAVOR DIGITAR 1 O 2")
            menu2(archivo)
    except:#si hay algún error imprime que existe un error y regresa la funcion menu2
        print("FAVOR DIGITAR 1 O 2")
        menu2(archivo)
def menu():
    try:#Aquí se validan errores para menu
        print("BIENVENIDO AL SIMULADOR DE INTÉRPRETE ITALI-NOVIS")
        print("Por favor, escoja la opción que desee digitando su número correspondiente")
        print("1.Nuevo Archivo")
        print("2.Compilar")
        opcion=int(input(">>"))#Input para que el usuario elija la opcion del menu que desee
        if opcion==1:
            crear()#Aquí se llama a la funcion "crear"
        elif opcion==2:
            print("No existe ningún archivo para compilar!\nPor Favor, cree un archivo primero")
            menu()
        else:
            print("FAVOR DIGITAR 1 O 2")
            menu()
    except:#si hay algún error imprime que existe un error y regresa la funcion menu
        print("FAVOR DIGITAR 1 O 2")
        menu()
menu()
