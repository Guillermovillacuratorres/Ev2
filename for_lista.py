
nombre = "Hola soy Pedro"
contador = -1
print(nombre[4])
for inicio in nombre:
    contador += 1
    if inicio == 'P':
        print("Encontre la " +  nombre[contador] + " en la posicion ", contador)
    if inicio == 'y':
        print("Encontre la y")
        #break