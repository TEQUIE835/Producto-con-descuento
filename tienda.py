#se inicia saludando al usuario
print("Hola, que producto busca validar el dia de hoy?")



#Creamos una variable para generar un ciclo y que el programa no se cierre hasta que le digamos
salir=bool(False)


#creamos el ciclo
while salir!=True:

#empezamos solicitando la informacion
    prod=str(input("\nEl nombre de tu producto: "))
    
    #Utilizamos ciclos while y Try para verificar que la informacion pueda ser aceptada
    
    while True:
        try:
            prec=float(input("\nIngrese el precio unitario: "))
            if prec >0:
                break
            else: 
                print("\nIngrese un precio valido")
        except: 
            print("\nIngrese un precio valido")
    while True:
        try:
            cant=int(input("\nIngrese la cantidad deseada: "))
            if cant >0:
                break
            else: 
                print("\nIngrese una cantidad valida")
        except: 
            print("\nIngrese una cantidad valida")
    des=str(input("\nTiene descuento? Y/N "))
    

    #Validamos si el producto posee un descuento
    if des=="Y" or des=="y":
            while True:
                try:
                    desc=int(input("\nIngrese el descuento: "))
                    if 100>= desc >0:
                        break
                    else: 
                        print("\nIngrese un descuento valido")
                except: 
                    print("\nIngrese un descuento valido")
                
                

            #Empezamos sacando el precio total sin descuento
            tot=prec*cant
            print(f"\nEl precio total de tu producto {prod} sin descuento aplicado es: {tot}\n")


            #Sacamos el descuento
            baj=(tot*desc)/100
            todesc=tot-baj
            #Mostramos al usuario el precio con descuento
            print(f"Su producto {prod} Con descuento cuesta: {todesc}")

            #Cerramos el while
            salir=True


    elif des=="N" or des=="n":

        
        

            #Se saca el total
            tot=prec*cant


            #Se imprime el total
            print(f"El precio total de tu producto {prod} es: {tot}\n")

            #Cerramos while
            salir=True
