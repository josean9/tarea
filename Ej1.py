posiciones_destino = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}
def inicio():
    n = int(input("Cuantos movimientos?"))
    print(calcular_movimientos_validos(n))
def metodo(moves,lista,contador,posiciones_destino):
        lista2=[]
        if contador==1:
            for i in range(10):
                for t in posiciones_destino[i]:
                    lista.append(t)
                   
                    
        else:
            for i in lista:
                
                
                
                i = int(i)

                for t in posiciones_destino[i]:
                    #print(t,posiciones_destino[i],"oa")
                    lista2.append(t)
            lista=[]
            lista.extend(lista2)
        if contador == moves:
            print(len(lista2))
            pass
        else:
            
            metodo(moves,lista,contador+1,posiciones_destino)            

def calcular_movimientos_validos(movimientos):
    numero = 0
    lista = []
    if movimientos == 1:
        for i in posiciones_destino:
            numero += len(posiciones_destino[i])
        return numero
    elif movimientos >1:
        print(metodo(movimientos,lista,1,posiciones_destino))
        return "Programa terminado"

print(calcular_movimientos_validos(3))