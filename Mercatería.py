def Mercateria () :
    
    """ Se solicita la información personal del cliente, Cedula y Rol.
    En Rol sólo es válido Estuiante o Profesor, asegúsere de
    escribirlos bien """

    print ( " ---------------------------------------------- " )  
    print ( " Información del cliente " )
    print ( " ---------------------------------------------- " )
    Dato_1 = str ( input ( " Cédula : " ) )
    Dato_2 = str ( input ( " Rol : " ) )

    """ Registre la infromación del producto """

    print ( " ---------------------------------------------- " )
    print ( " Registrar prodcuto " )
    print ( " ---------------------------------------------- " )
    Dato_3 = str ( input ( " Código del prodcuto : " ) )
    Dato_4 = int ( input ( " Cántidad de unidades : " ) )
    Dato_5 = int ( input ( " Precio del producto : " ) )
    
    """ Encuentra el valor de los prodcutos sin el descuento """

    Sin_Descuento = Dato_4 * Dato_5

    """ A partir del Rol aplica el descuento para encontrar el precio
    final  """
    
    if ( Dato_2 == "Estudiante" ) :
        Total = Sin_Descuento - ( Sin_Descuento * 0.4 )
    elif ( Dato_2 == "Profesor" ) :
        Total = Sin_Descuento - ( Sin_Descuento * 0.2 )
    else :
        print ( " ---------------------------------------------- " )
        print ( " ERROR : " )
        print ( " Asegúrese de escribir bien todos los parámetros. " )
        print ( " En Rol solo es válido poner Estudiante o Profesor. ")
        print ( " Vuelva a intentarlo. " )
        Total = 0
        
    """ Imprime en pantalla los resultados """

    print ( " ---------------------------------------------- " )
    print ( "El", Dato_2, "con cédula", Dato_1, "debe pagar", Total,
            "por el producto", Dato_3)
    print ( " ---------------------------------------------- " )
    

Mercateria ()
    
