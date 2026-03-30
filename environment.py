class Grid:
    def __init__(self, n, obstacles, items, start, goal, energy):
        self.n = n
        self.obstacles = set(obstacles)
        self.items = items
        self.start = start
        self.goal = goal
        self.energy = energy

    def is_valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and (x, y) not in self.obstacles

    def get_neighbors(self, state):
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        neighbors = []

        # MOVE
        for dx, dy in dirs:
            nx, ny = state.x + dx, state.y + dy
            if self.is_valid(nx, ny) and state.energy > 0:
                neighbors.append(type(state)(
                    nx, ny,
                    state.remaining_items,
                    state.collected_items,
                    state.energy - 1
                ))

        # PICKUP
        if (state.x, state.y) in state.remaining_items:
            new_r = set(state.remaining_items)
            new_c = set(state.collected_items)
            new_r.remove((state.x, state.y))
            new_c.add((state.x, state.y))

            neighbors.append(type(state)(
                state.x, state.y,
                new_r,
                new_c,
                state.energy
            ))

        return neighbors