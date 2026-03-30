from state import State
from environment import Grid
from heuristics import h1, h2
from algorithms import bfs, ucs, greedy, astar
from visualization import animate

from test_cases import *

# ---------------- SELECT TEST CASE ----------------
cases = {
    "easy": easy,
    "medium": medium,
    "hard": hard,
    "no_path": no_path,
    "low_energy": low_energy,
    "tradeoff": tradeoff,
    "maze": maze,
    "many_items": many_items,
    "priority_trap": priority_trap,
    "straight_vs_detour": straight_vs_detour,
    "small_easy": small_easy,
    "small_obstacle": small_obstacle,
    "small_tradeoff": small_tradeoff,
    "small_energy": small_energy,
    "small_maze": small_maze,
    "small_no_path": small_no_path,
    "small_many_items": small_many_items
}

print("Available test cases:")
for k in cases:
    print("-", k)

choice = input("\nChoose test case: ").strip()
config = cases.get(choice, medium)()

grid = Grid(**config)

# ---------------- SELECT ALGORITHM ----------------
algo = input("Choose algorithm (BFS / UCS / Greedy / A*): ").strip()

# ---------------- SELECT HEURISTIC ----------------
h_choice = input("Choose heuristic (h1 / h2): ").strip()
h = h1 if h_choice == "h1" else h2


# ---------------- RUN ----------------
if algo == "BFS":
    path, explored = bfs(grid, State)
elif algo == "UCS":
    path, explored = ucs(grid, State)
elif algo == "Greedy":
    path, explored = greedy(grid, State, h)
else:
    path, explored = astar(grid, State, h)


# ---------------- OUTPUT ----------------
print("\n=== RESULT ===")
print("Nodes Expanded:", len(explored))
print("Path Length:", len(path) if path else -1)

if path is None:
    print("No feasible solution within energy constraints")


# ---------------- VISUALIZE ----------------
animate(grid, explored, path)