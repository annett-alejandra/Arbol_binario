from Node import Nodo

class Arbol:
    def __init__(self):
        self.raiz = None
        
    # --- Getters y Setters ---
    
    def getRaiz(self):
        return self.raiz
        
    def setRaiz(self, raiz):
        self.raiz = raiz

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print("-" * 9)

def main():
    a = Arbol()
    nodo_actual = Nodo()
    a.setRaiz(nodo_actual)
    
    turno = 'X'
    jugadas = 0
    
    print("¡Bienvenido al Tres en Raya con Árboles!")
    
    while jugadas < 9:
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
            
        # Crear un nuevo nodo (nueva jugada)
        nuevo_nodo = Nodo()
        
        # Copiar el tablero actual al nuevo nodo
        nuevo_tablero = [f[:] for f in tablero_actual]
        nuevo_tablero[fila][col] = turno
        nuevo_nodo.setTablero(nuevo_tablero)
        
        # Conectar el nuevo estado como hijo del estado anterior
        nodo_actual.agregarHijo(nuevo_nodo)
        
        # Moverse por el árbol hacia el nuevo hijo (avanzar el estado del juego)
        # Como acabamos de agregarlo, es el último en la lista de hijos
        nodo_actual = nodo_actual.getHijos()[-1]
        
        jugadas += 1
        turno = 'O' if turno == 'X' else 'X'
        
    print("\n--- FIN DEL JUEGO ---")
    imprimir_tablero(nodo_actual.getTablero())

if __name__=='__main__':
    main()
