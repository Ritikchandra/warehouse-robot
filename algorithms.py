import heapq, itertools
from collections import deque


# ---------------- PATH RECONSTRUCTION ----------------
def reconstruct(parent, s):
    path = []
    while s in parent:
        path.append((s.x, s.y))
        s = parent[s]
    path.append((s.x, s.y))
    return path[::-1]


# ---------------- SCORE ----------------
def score(grid, s):
    return sum(grid.items[i] for i in s.collected_items)


# =====================================================
# BFS
# =====================================================
def bfs(grid, State):
    start = State(*grid.start, set(grid.items.keys()), set(), grid.energy)

    q = deque([start])
    visited = set()
    parent = {}
    explored = []

    best_goal, best_score = None, -1

    while q:
        s = q.popleft()

        explored.append((s.x, s.y, score(grid, s)))

        if s.energy < 0:
            continue

        if (s.x, s.y) == grid.goal:
            sc = score(grid, s)
            if sc > best_score:
                best_score, best_goal = sc, s
            continue

        if s in visited:
            continue
        visited.add(s)

        for n in grid.get_neighbors(s):
            if n.energy < 0:  
                continue
            parent[n] = s
            q.append(n)

    if best_goal is not None:
        return reconstruct(parent, best_goal), explored
    else:
        return None, explored


# =====================================================
# UCS
# =====================================================
def ucs(grid, State):
    counter = itertools.count()
    start = State(*grid.start, set(grid.items.keys()), set(), grid.energy)

    pq = [(0, next(counter), start)]
    visited, parent = {}, {}
    explored = []

    best_goal, best_score = None, -1

    while pq:
        cost, _, s = heapq.heappop(pq)

        explored.append((s.x, s.y, score(grid, s)))

        if s.energy < 0:
            continue

        if (s.x, s.y) == grid.goal:
            sc = score(grid, s)
            if sc > best_score:
                best_score, best_goal = sc, s
            continue

        key = (s.x, s.y, s.remaining_items)
        if key in visited and visited[key] >= s.energy:
            continue
        visited[key] = s.energy

        for n in grid.get_neighbors(s):
            if n.energy < 0:
                continue
            heapq.heappush(pq, (cost + 1, next(counter), n))
            parent[n] = s

    if best_goal is not None:
        return reconstruct(parent, best_goal), explored
    else:
        return None, explored


# =====================================================
# GREEDY
# =====================================================
def greedy(grid, State, h):
    counter = itertools.count()
    start = State(*grid.start, set(grid.items.keys()), set(), grid.energy)

    pq = [(0, next(counter), start)]
    visited, parent = {}, {}
    explored = []

    best_goal, best_score = None, -1

    while pq:
        _, _, s = heapq.heappop(pq)

        explored.append((s.x, s.y, score(grid, s)))

        if s.energy < 0:
            continue

        if (s.x, s.y) == grid.goal:
            sc = score(grid, s)
            if sc > best_score:
                best_score, best_goal = sc, s
            continue

        key = (s.x, s.y, s.remaining_items)
        if key in visited and visited[key] >= s.energy:
            continue
        visited[key] = s.energy

        for n in grid.get_neighbors(s):
            if n.energy < 0:
                continue
            heapq.heappush(pq, (h(n, grid.goal), next(counter), n))
            parent[n] = s

    if best_goal is not None:
        return reconstruct(parent, best_goal), explored
    else:
        return None, explored


# =====================================================
# A*
# =====================================================
def astar(grid, State, h, lam=1.0):
    counter = itertools.count()
    start = State(*grid.start, set(grid.items.keys()), set(), grid.energy)

    pq = [(0, 0, next(counter), start)]
    visited, parent = {}, {}
    explored = []

    best_goal, best_score = None, -1

    while pq:
        f, g, _, s = heapq.heappop(pq)

        explored.append((s.x, s.y, score(grid, s)))

       
        if s.energy < 0:
            continue

        if (s.x, s.y) == grid.goal:
            sc = score(grid, s)
            if sc > best_score:
                best_score, best_goal = sc, s
            continue

        key = (s.x, s.y, s.remaining_items)
        if key in visited and visited[key] >= s.energy:
            continue
        visited[key] = s.energy

        for n in grid.get_neighbors(s):
            if n.energy < 0: 
                continue

            g2 = g + 1
            reward = score(grid, n)
            f2 = g2 + h(n, grid.goal) - lam * reward

            heapq.heappush(pq, (f2, g2, next(counter), n))
            parent[n] = s

    if best_goal is not None:
        return reconstruct(parent, best_goal), explored
    else:
        return None, explored