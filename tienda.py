#se inicia saludando al usuario
print("Hola, que producto busca validar el dia de hoy?")



#Creamos una variable para generar un ciclo y que el programa no se cierre hasta que le digamos
salir=False


#creamos el ciclo
while salir!=True:

#empezamos solicitando la informacion
    print("")
    prod=str(input("El nombre de tu producto: "))
    print("")
    prec=float(input("Ingrese el precio unitario: "))
    print("")
    cant=int(input("Ingrese la cantidad deseada: "))
    print("")
    des=str(input("Tiene descuento? Y/N "))
    print("")

    #Validamos si el producto posee un descuento
    if des=="Y":
        desc=int(input("Ingrese el descuento si aplica: "))
        print("")


        #se valida la informacion
        if prec>0 and cant>0 and desc>0 and desc<=100:

            #Empezamos sacando el precio total sin descuento
            tot=prec*cant

            print("El precio total de tu producto " + prod+ " sin descuento aplicado es: ", tot)
            print("")

            #Validamos si el producto cuenta con descuento
            if desc>0:

                #Sacamos el descuento
                baj=(tot*desc)/100
                todesc=tot-baj

                #Mostramos al usuario el precio con descuento
                print("Su producto " + prod + " Con descuento cuesta: ", todesc)

                #Cerramos el while
                salir=True


        #Si el producto no tiene descuento se cierra el ciclo solamente
            else: 
                salir=True



        elif prec<=0:
            print("Dijite un precio valido")
        elif cant<=0:
            print("Dijite una cantidad valida")
        elif desc<0 or desc>100:
            print("Dijite un descuento valido")
        else: 
            print("Hubo un error, intente de nuevo")


    elif des=="N":

        #Se valida que el precio y la cantidad sean validos
        if prec>0 and cant>0:

            #Se saca el total
            tot=prec*cant


            #Se imprime el total
            print("El precio total de tu producto " + prod+ " es: ", tot)
            print("")

            #Cerramos while
            salir=True


        elif prec<=0:
            print("Dijite un precio valido")
        elif cant<=0:
            print("Dijite una cantidad valida")
        else: print("Hubo un error, intente de nuevo")