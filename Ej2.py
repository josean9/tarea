def comprobar(reinas, fila, columna):
    for i in range(fila):
        if reinas[i][columna] == 1:
            return False
        if columna - i >= 0 and reinas[fila - i][columna - i] == 1:
            return False
        if columna + i < len(reinas) and reinas[fila - i][columna + i] == 1:
            return False
    return True

def resolver_n_reinas(n):
    def encontrar_solucion(fila):
        if fila == n:
            return [list(row) for row in reinas]
        soluciones = []
        for columna in range(n):
            if comprobar(reinas, fila, columna):
                reinas[fila][columna] = 1
                soluciones.extend(encontrar_solucion(fila + 1))
                reinas[fila][columna] = 0
        return soluciones

    reinas = [[0] * n for _ in range(n)]
    soluciones = encontrar_solucion(0)
    return soluciones

n = 4 
soluciones = resolver_n_reinas(n)
print("Número de soluciones:", len(soluciones))
