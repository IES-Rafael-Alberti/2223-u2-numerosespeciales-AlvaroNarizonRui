def calcular_suma_pares_no_multiplos_de_3(inicio,fin):
    contenedor_pares = 0
    if numero_inicial or numero_final < 1:
        raise ValueError
    else:
        for i in range(inicio,fin,1):
            if i % 2 == 0:
                if i % 3 != 0:
                    contenedor_pares += i
        return contenedor_pares


def calcular_suma_impares_no_multiplos_de_3(inicio,fin):
    contenedor_impares = 0
    if numero_inicial or numero_final < 1:
        raise ValueError
    else:
        for i in range(inicio,fin,1):
            if i % 2 != 0:
                if i % 3 != 0:
                    contenedor_impares += i
        return contenedor_impares



if __name__ == '__main__':
    try:
        #Entrada
        numero_inicial = int(input("Ingrese el numero inicial : "))
        numero_final = int(input("Ingrese el numero final: "))
        eleccion = input("Desea calcular la suma de pares o impares?? \n Escriba (pares/impares) : ")
        #Procesamiento
        if eleccion.lower() == "pares":
            pares = calcular_suma_pares_no_multiplos_de_3(numero_inicial,numero_final)
            #Salida
            print(f"La suma de los números pares que no son múltiplos de 3 entre {numero_inicial} y {numero_final} es: \n {pares}")
        elif eleccion.lower() == "impares":
            impares = calcular_suma_impares_no_multiplos_de_3(numero_inicial,numero_final)
            #Salida
            print(f"La suma de los números impares que no son múltiplos de 3 entre {numero_inicial} y {numero_final} es: \n {impares}")
    except ValueError:
        print("No se puede usar un valor final o inicial menor que 1")

    


