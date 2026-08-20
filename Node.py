'''
title: clase Nodo
description: Clase Nodo para juego Tres en Raya (Matriz 3x3)
'''

class Nodo:
    '''Método que inicializa la clase nodo'''
    def __init__(self):
        # Matriz 3x3 para el tablero
        self.tablero = [['-' for _ in range(3)] for _ in range(3)]
        # Lista de hijos (hasta 9 posibles jugadas)
        self.hijos = []
        
    # --- Getters y Setters ---
    
    def getTablero(self):
        return self.tablero
        
    def setTablero(self, tablero):
        self.tablero = tablero
        
    def getHijos(self):
        return self.hijos
        
    def setHijos(self, hijos):
        self.hijos = hijos
        
    def agregarHijo(self, hijo):
        if len(self.hijos) < 9:
            self.hijos.append(hijo)
