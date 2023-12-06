
#Para mostrar el total de libros
def mostrar_numero_total(biblioteca) -> int:
    total = 0
    for valor in biblioteca.values():
        total += int(valor)
    return total

#para agregar un nuevo genero
def agregar_nvo(biblioteca):
    nvo_genero = input("Nombre del Genero: ")
    cant_libro = int(input("Ingrese la cantidad de libros: "))
    biblioteca[nvo_genero] = cant_libro

#para eliminar un genero
def eliminar_genero(biblioteca):
    genero_eliminar = input("Nombre del genero a eliminar: ")
    if genero_eliminar in biblioteca:
        del biblioteca[genero_eliminar]
        print("Eliminado Correctamente")
    else:
        print(f"El genero: '{genero_eliminar}' no existe en tu biblioteca!")

#Para mostrar generos y cantidades
def mostrar(biblioteca):
    for clave, valor in biblioteca.items():
        print(clave, valor)

#Para mostrar los libros en los cuales hay menos de 10 unidades
def cant_menor10(biblioteca):
    for clave, valor in biblioteca.items():
        if(valor <= 10):
            print(clave)

#Solo es un menu que devuelve los datos de ingresos que solicitamos
def menu() -> str:
    ingreso = "Menu Principal:\n"
    ingreso += "1 - Mostrar total de libros\n"
    ingreso += "2 - Agregar un nuevo genero\n"
    ingreso += "3 - Eliminar un genero\n"
    ingreso += "4 - Mostrar generos y cantidades\n"
    ingreso += "5 - Libros que tengan menos de 10un\n"
    ingreso += "0 - Salir\n"
    return ingreso

if __name__ == "__main__":

    biblioteca = {
        'matematica':30,
        'biologia':50,
        'estadistica':5,
        'tecnologia':9,
        'ciencias':30
    }
    #print(menu())
    menuprincipal = int(input(menu()))
    while menuprincipal != 0:
        if menuprincipal == 1:
            print()
            print("El numero total de libros que hay es: ", mostrar_numero_total(biblioteca))
            print("\n#####")
        elif menuprincipal == 2:
            agregar_nvo(biblioteca)
            print("\n\tAgregando...")
            print("Agregado con exito")
            print("\n#####")
        elif menuprincipal == 3:
            print("\n\tEliminando...")
            eliminar_genero(biblioteca)
            print("\n#####")
        elif menuprincipal == 4:
            print("\nMostrando todos los generos con sus cantidades")
            mostrar(biblioteca)
            print("\n#####")
        elif menuprincipal == 5:
            print("\nLibros con cantidad menor a 10")
            cant_menor10(biblioteca)
            print("\n#####")
        else:
            print("Por favor digite una opcion correcta")

        menuprincipal = int(input(menu()))
        