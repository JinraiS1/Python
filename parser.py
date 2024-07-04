def buscar_cadena():
    cadena = input("Introduce la cadena de texto que quieres buscar: ") #Introducimos la cadena a buscar
    nombre_archivo = input("Introduce el nombre del archivo de texto: ") #Introducimos el fichero donde buscar la cadena

   #Abre el fichero indicado y lo lee
    with open(nombre_archivo, 'r') as archivo:  
        lineas = archivo.readlines()

    #Busca la cadena indicada en cada línea del fichero y, por cada match, agrega una línea en la variable "resultados"
    resultados = [linea for linea in lineas if cadena in linea]
    
    #Vuelca los resultados obtenidos en la variable "resultados" en un fichero llamado "resultados.txt"

    with open('resultados.txt', 'w') as archivo_resultados:
        for resultado in resultados:
            archivo_resultados.write(resultado)

buscar_cadena()
