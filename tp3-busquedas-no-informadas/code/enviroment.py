import random
import gymnasium as gym

def generate_random_map_custom(size_desc, hole_prob, seed = None, slippery = False):
    if seed != None:
        random.seed(seed)
    desc = [['F' for _ in range(size_desc)] for _ in range(size_desc)]
    hole_celds = round(size_desc * size_desc * hole_prob)
    for i in range(hole_celds):
        check = False
        while check != True:
            rx = random.randint(0, (size_desc) - 1)
            ry = random.randint(0, (size_desc) - 1)
            # print(rx,ry)
            if desc[rx][ry] != 'H':
                desc[rx][ry] = 'H'
                check = True
    rx = random.randint(0, (size_desc) - 1)
    ry = random.randint(0, (size_desc) - 1)
    # POSICION INICIAL AGENTE
    desc[rx][ry] = "S"
    rx = random.randint(0, (size_desc) - 1)
    ry = random.randint(0, (size_desc) - 1)
    # POSICION GOAL
    desc[rx][ry] = "G"
    env = gym.make("FrozenLake-v1", desc=desc, render_mode="human", is_slippery = slippery)
    return env, desc

# env, desc = generate_random_map_custom(4, 0.5, 2)
# print(desc)