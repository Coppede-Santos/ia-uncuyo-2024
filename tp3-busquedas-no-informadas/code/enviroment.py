import gymnasium as gym
env = gym.make("FrozenLake-v1", render_mode="human")

##Obtener informacion del entorno:

print("Numero de estados:", env.observation_space.n)
print("Numero de acciones:", env.action_space.n)


##Ejecutar un episodio basico:

state = env.reset()
print("Posicion inicial del agente:", state[0])
done = truncated = False
while not (done or truncated):
    action = env.action_space.sample() # Accion aleatoria
    next_state, reward, done, truncated, _ = env.step(action)
    print(f"Accion: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
    print(f"¿Gano? (encontro el objetivo): {done}")
    print(f"¿Freno? (alcanzo el maximo de pasos posible): {truncated}\n")
    state = next_state