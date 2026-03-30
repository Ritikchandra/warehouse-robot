import time
import csv

def run_all(grid, State, algos):
    results = []

    for name, func in algos:
        start = time.time()
        path, nodes = func()
        t = time.time() - start

        results.append([name, nodes, round(t,4), len(path) if path else -1])

    with open("results.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(["Algo","Nodes","Time","Path"])
        writer.writerows(results)

    return results