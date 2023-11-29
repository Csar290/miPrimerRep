titulo = "CREA UNA CUENTA DE FEISBUCK"
print(titulo.center(133))

nombre = input("¿Como quieres que te llamen?: ")
correo = input("Ingrese su correo: ")
contraseña = input("Ingrese una contraseña: ")
contraseña_dos = input("Confirme su contraseña: ")

if contraseña_dos == contraseña:
    print("\nSu cuenta ha sido creada con exito.")
    print("Ahora ponga los datos que acaba de registrar para ingresar a la plataforma.")

    correo_dos = input("\nIngrese su correo: ")
    contraseña_tres = input("Ingrese su contraseña: ")

    if correo_dos == correo and contraseña_tres == contraseña:
        print("\nHola ", nombre, " Bienvenido a Feisbuck. ¿Que haremos hoy?.")

    else:
        print("Tu correo o contraseña son incorrectas. Vuelve a intentarlo.")


else:
    print("\nLa contraseña no coincide. Vuelve a intentarlo.")
    


   




    
