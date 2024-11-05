prereq = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]

preMap = {}

for crs, pre in prereq:
    if crs not in preMap:
        preMap[crs] = []
    if pre not in preMap:
        preMap[pre] = []
    preMap[crs].append(pre)

preMap

stack = [0]
visited = set()
visited.add(0)
top_sort = []
while stack:
    crs = stack.pop()
    for nei in preMap[crs]:
        if nei not in visited:
            stack.append(nei)
            visited.add(nei)
    top_sort.append(nei)

top_sort
