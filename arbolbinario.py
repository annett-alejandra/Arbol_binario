from Node import Nodo

class Arbol:
    def __init__(self):
        self.raiz = None
        
    # --- Getters y Setters ---
    
    def getRaiz(self):
        return self.raiz
        
    def setRaiz(self, raiz):
        self.raiz = raiz
        
    def contar_nodos(self, nodo):
        # Recorrido simple para contar cuántos estados de juego se guardaron
        if nodo is None:
            return 0
        total = 1
        for hijo in nodo.getHijos():
            total += self.contar_nodos(hijo)
        return total

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print("-" * 9)
def verificar_ganador(tablero, jugador):
    # Revisar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True
    # Revisar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def main():
    a = Arbol()
    nodo_actual = Nodo()
    a.setRaiz(nodo_actual)
    
    turno = 'X'
    jugadas = 0
    ganador = False
    
    print("¡Bienvenido al Tres en Raya con Árboles!")
    
    while jugadas < 9 and not ganador:
        print(f"\nTurno del jugador {turno}")
        imprimir_tablero(nodo_actual.getTablero())
        
        try:
            fila = int(input("Elige fila (0, 1, 2): "))
            col = int(input("Elige columna (0, 1, 2): "))
        except ValueError:
            print("Por favor ingresa números válidos.")
            continue
            
        if fila < 0 or fila > 2 or col < 0 or col > 2:
            print("Posición inválida. Debe ser 0, 1 o 2.")
            continue
            
        tablero_actual = nodo_actual.getTablero()
        if tablero_actual[fila][col] != '-':
            print("Esa casilla ya está ocupada.")
            continue
            
        nuevo_nodo = Nodo()
        nuevo_tablero = [f[:] for f in tablero_actual]
        nuevo_tablero[fila][col] = turno
        nuevo_nodo.setTablero(nuevo_tablero)
        
        nodo_actual.agregarHijo(nuevo_nodo)
        nodo_actual = nodo_actual.getHijos()[-1]
        
        if verificar_ganador(nodo_actual.getTablero(), turno):
            ganador = True
        else:
            turno = 'O' if turno == 'X' else 'X'
            jugadas += 1
        
    print("\n--- FIN DEL JUEGO ---")
    imprimir_tablero(nodo_actual.getTablero())
    
    if ganador:
        print(f"¡El jugador {turno} ha GANADO!")
    else:
        print("¡Es un EMPATE!")
        
    # Recorrido del árbol para verificar que guarda los nodos
    total = a.contar_nodos(a.getRaiz())
    print(f"\n[Info del Árbol] Se han generado {total} nodos (estados del tablero) durante esta partida.")

if __name__=='__main__':
    main()
