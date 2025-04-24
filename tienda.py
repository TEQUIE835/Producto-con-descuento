#se inicia saludando al usuario
print("Hola, que producto busca validar el dia de hoy?")



#Creamos una variable para generar un ciclo y que el programa no se cierre hasta que le digamos
salir=bool(False)


#creamos el ciclo
while salir!=True:

#empezamos solicitando la informacion
    print("")
    prod=str(input("El nombre de tu producto: "))
    
    #Utilizamos ciclos while y Try para verificar que la informacion pueda ser aceptada
    
    while True:
        try:
            print("")
            prec=float(input("Ingrese el precio unitario: "))
            if prec >0:
                break
            else: 
                print("")
                print("Ingrese un precio valido")
        except: 
            print("")
            print("Ingrese un precio valido")
    while True:
        try:
            print("")
            cant=int(input("Ingrese la cantidad deseada: "))
            if cant >0:
                break
            else: 
                print("")
                print("Ingrese una cantidad valida")
        except: 
            print("")
            print("Ingrese una cantidad valida")
    print("")
    des=str(input("Tiene descuento? Y/N "))
    

    #Validamos si el producto posee un descuento
    if des=="Y" or des=="y":
            while True:
                try:
                    print("")
                    desc=int(input("Ingrese el descuento: "))
                    if 100>= desc >0:
                        break
                    else: 
                        print("")
                        print("Ingrese un descuento valido")
                except: 
                    print("")
                    print("Ingrese un descuento valido")
                
                

            #Empezamos sacando el precio total sin descuento
            tot=prec*cant
            print("")
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


    elif des=="N" or des=="n":

        
        

            #Se saca el total
            tot=prec*cant


            #Se imprime el total
            print("El precio total de tu producto " + prod+ " es: ", tot)
            print("")

            #Cerramos while
            salir=True
