import random

class AgentAle:
    def __init__(self,env):
        self.env=env
    def up(self):self.env.accept_action("Arriba")
    def down(self):self.env.accept_action("Abajo")
    def left(self):self.env.accept_action("Izquierda")
    def right(self):self.env.accept_action("Derecha")
    def suck(self):self.env.accept_action("Limpiar") # Limpia
    def idle(self):self.env.accept_action("NoHacerNada") # no hace nada
    def perspective(self):self.env.is_dirty() # sensa el entorno
    def think(self):
        action = random.choice(["Arriba", "Abajo", "Izquierda", "Derecha","Limpiar","NoHacerNada"])
        self.env.accept_action(action)