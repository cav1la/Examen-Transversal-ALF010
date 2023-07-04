import os

while True:
    os.system("clear")
    print("========BIENVENIDO ADMIN LINUX========")
    print("a.- Administración de usuarios")
    print("b.- Administración de archivos")
    print("c.- Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "a":
        while True:
            os.system("clear")
            print("========ADMIN USUARIOS========")
            print("a.- Crear usuario")
            print("b.- Eliminar usuario")
            print("c.- Volver")
            
            opcion2 = input("Ingrese su opción: ")
            
            if opcion2 == "a":
                nombre_usuario = input("Ingrese nombre de usuario a crear: ")
                os.system(f"adduser {nombre_usuario}")
                input("Presione Enter para continuar...")
                
            elif opcion2 == "b":
                nombre_usuario = input("Ingrese nombre de usuario a eliminar: ")
                resultado = os.system(f"deluser {nombre_usuario}")
                if resultado != 0:
                    print(f"Error: el usuario {nombre_usuario} no existe")
                else:
                    print(f"El usuario {nombre_usuario} ha sido eliminado correctamente")
                input("Presione Enter para continuar...")
                
            elif opcion2 == "c":
                break
                
            else:
                input("Opción inválida. Presione Enter para continuar...")
                
    elif opcion == "b":
        while True:
            os.system("clear")
            print("========ADMIN ARCHIVOS========")
            print("a.- Crear archivo")
            print("b.- Eliminar archivo")
            print("c.- Volver")
            
            opcion2 = input("Ingrese su opción: ")
            
            if opcion2 == "a":
                nombre_archivo = input("Ingrese nombre de archivo a crear: ")
                os.system(f"touch {nombre_archivo}")
                input("Presione Enter para continuar...")
                
            elif opcion2 == "b":
                nombre_archivo = input("Ingrese nombre de archivo a eliminar: ")
                resultado = os.system(f"rm {nombre_archivo}")
                if resultado != 0:
                    print(f"Error: el archivo {nombre_archivo} no existe")
                else:
                    print(f"El archivo {nombre_archivo} ha sido eliminado correctamente")
                input("Presione Enter para continuar...")
                
            elif opcion2 == "c":
                break
                
            else:
                input("Opción inválida. Presione Enter para continuar...")
                
    elif opcion == "c":
        break
        
    else:
        input("Opción inválida. Presione Enter para continuar...")
