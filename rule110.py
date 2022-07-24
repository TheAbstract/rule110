state = {-1}

def generate(state):
    next_state = set()
    for agent in state:
        if agent + 1 not in state:
            next_state.add(agent)

        if agent - 1 not in state:
            next_state.add(agent)
            next_state.add(agent - 1)

    return next_state

def display(state, iterations=32):
    alive, dead = '*', ' '
    interval = range(-iterations, 0)
    print(' '.join(alive if agent in state else dead for agent in interval))

if __name__ == '__main__':
    iterations = 32

    for _ in range(iterations):
        display(state)
        state = generate(state)
