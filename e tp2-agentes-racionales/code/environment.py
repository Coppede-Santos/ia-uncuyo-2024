import random

class Environment:
    def __init__(self, sizeX, sizeY, init_posX, init_posY, dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.init_posX = init_posX  
        self.init_posY = init_posY
        self.dirt_rate = dirt_rate
        
        # Crear la matriz con probabilidad de suciedad
        self.matriz = [[random.random() < dirt_rate for _ in range(sizeY)] for _ in range(sizeX)]
        self.suciedadinicial = sum(sum(fila) for fila in self.matriz)

    def accept_action(self, action):
        if action == "Abajo" and self.init_posX > 0:
            self.init_posX -= 1
        elif action == "Arriba" and self.init_posX < self.sizeX - 1:
            self.init_posX += 1
        elif action == "Izquierda" and self.init_posY > 0:
            self.init_posY -= 1
        elif action == "Derecha" and self.init_posY < self.sizeY - 1:
            self.init_posY += 1
        elif action == "Limpiar":
            if self.matriz[self.init_posX][self.init_posY]:  # Solo limpia si está sucio
                self.matriz[self.init_posX][self.init_posY] = False
                
        elif action == "NoHacerNada":
            pass 
        
    def is_dirty(self):
        return self.matriz[self.init_posX][self.init_posY]

    def get_performance(self):
        count = sum(sum(fila) for fila in self.matriz)
        cleaned = self.suciedadinicial - count
        
        return cleaned
            
    def print_enviroment(self):
        for fila in self.matriz:
            print(fila)


#m = Environment(2,2,0,0,1)
#m.print_enviroment()
#m.accept_action("Limpiar")
#m.accept_action("Derecha")
#m.accept_action("Limpiar")
#m.accept_action("Arriba")
#m.accept_action("Limpiar")
#m.accept_action("Izquierda")
#m.accept_action("Limpiar")
#m.print_enviroment()
#print(m.get_performance())