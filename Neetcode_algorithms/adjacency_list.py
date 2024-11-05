from collections import deque


# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    elif dst not in adjList:
        adjList[dst] = []

    adjList[src].append(dst)


def dfs(start, target, adjlist, visit):
    if start in visit:
        return 0
    if start == target:
        return 1

    c = 0
    visit.add(start)

    for neighbor in adjList[start]:
        c += dfs(neighbor, target, adjList, visit)
    visit.remove(start)
    return c


dfs("A", "E", adjList, set())


def bfs(start, target, adjlist):
    step = 0
    visit = set()
    visit.add(start)

    queue = deque(start)

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return step
            else:
                for neighbor in adjList[curr]:
                    visit.add(neighbor)
                    queue.append(neighbor)

        step += 1
    return step


bfs("A", "E", adjList)
