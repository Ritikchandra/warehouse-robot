def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


# ---------- h1 ----------
def h1(state, goal):
    if not state.remaining_items:
        return manhattan((state.x, state.y), goal)

    return min(
        manhattan((state.x, state.y), i) + manhattan(i, goal)
        for i in state.remaining_items
    )


# ---------- MST ----------
def mst(points):
    if len(points) <= 1:
        return 0

    points = list(points)
    visited = {points[0]}
    cost = 0

    while len(visited) < len(points):
        best = float('inf')
        nxt = None

        for v in visited:
            for u in points:
                if u not in visited:
                    d = manhattan(v, u)
                    if d < best:
                        best = d
                        nxt = u

        cost += best
        visited.add(nxt)

    return cost


# ---------- h2 ----------
def h2(state, goal):
    pts = list(state.remaining_items) + [(state.x, state.y), goal]
    return mst(pts)