#Hecho por Antonio Valdés Hernández // 3CM1
import time
inicio = time.time()
def burb(arr):
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]

def burbop(arr):
    n= len(arr)
    xd= True
    while xd:
        xd= False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                arr[i-1],arr[i]= arr[i],arr[i-1]
                xd= True
        n-=1

def main():
    print("Seleccione un método de ordenamiento:")
    print("1] Burbuja")
    print("2] Burbuja Optimizada")
    
    elec = int(input("Ingrese su elección: "))
    
    if elec not in [1,2]:
        print("Opción inválida")
        return
    
    tam = int(input("Ingrese el tamaño de la lista: "))
    
    arr = []
    for i in range(tam):
        print("Ingrese el elemento",i+1,": ")
        element = int(input())
        arr.append(element)
    
    if elec == 1:
        burb(arr)
        print("Lista ordenada: ", arr)
    elif elec == 2:
        burbop(arr)
        print("Lista ordenada: ", arr)

if __name__ == "__main__":
    main()

fin = time.time()
print("Tiempo transcurrido:",fin-inicio)
