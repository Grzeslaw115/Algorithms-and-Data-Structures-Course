from queue import PriorityQueue
from queue import deque
#BFS
def bfs(G, s):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    time = [float('inf')] * n
    queue = deque()
    time[s] = 0
    visited[s] = True
    queue.append(s)
    while queue:
        vertex = queue.popleft()
        for i in G[vertex]:
            if visited[i] is False:
                visited[i] = True
                parent[i] = vertex
                queue.append(i)
    return 

#DFS
def dfs(G):
    def dfs_visit(G, u):
        nonlocal time
        time += 1
        visited[u] = True
        for neighbour in G[u]:
            if visited[neighbour] is False:
                parent[neighbour] = u
                dfs_visit(G, neighbour)
        time += 1
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    time = 0
    for i in range(n):
        if visited[i] is False:
            dfs_visit(G, i)
    return

#TOPOLOGICAL SORT
def top_sort(G):
    def dfs_visit(G, u):
        nonlocal time
        nonlocal result
        time += 1
        visited[u] = True
        for neighbour in G[u]:
            if visited[neighbour] is False:
                parent[neighbour] = u
                dfs_visit(G, neighbour)
        time += 1
        result.append(u)
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    result = []
    time = 0
    for i in range(n):
        if visited[i] is False:
            dfs_visit(G, i)
    return result[::-1]
    
#DIJKSTRA
def dijkstra(G, s):
    n = len(G)
    time = [float('inf')] * n
    visited = [False] * n
    queue = PriorityQueue()
    time[s] = 0
    queue.put((0,s))
    while queue.empty() is False:
        vertex = queue.get()[1]
        if visited[vertex] is True:
            continue
        for edge in G[vertex]:
            if time[edge[0]] > time[vertex] + edge[1]:
                time[edge[0]] = time[vertex] + edge[1]
                queue.put((time[edge[0]], edge[0]))
        visited[vertex] = True
    return time


#BELLMAN FORD
def bellman_ford(G, s):
    n = len(G)
    time = [float('inf')] * n
    time[s] = 0
    
    for i in range(n):
        for j in range(n):
            for k in G[j]:
                if time[j] == float('inf'):
                    continue
                if time[j] + k[1] < time[k[0]]:
                    time[k[0]] = time[j] + k[1]
    for i in range(n):
        for j in G[i]:
            if time[i] + j[1] < time[j[0]]:
                return None
    return time

#FLOYD WARSHALL
def floyd_warshall(G):
    n = len(G)
    for t in range(n):
        for x in range(n):
            for y in range(n):
                G[x][y] = min(G[x][y], G[x][t]+G[t][y])
    return G

#ALGORYTM PRIMA
def prim(G, s):
    n = len(G)
    visited = [False] * n
    queue = PriorityQueue()
    mst = []
    cost = 0
    queue.put((0, (s, None)))
    visited[s] = True

    while queue.empty() is False:
        c, e = queue.get()
        v = e[0]
        p = e[1]
        if visited[v] is False:
            cost += c
            mst.append((v, p))

        for neighbour in G[v]:
            n, weight = neighbour
            if visited[n] is False:
                queue.put((weight, (n, v)))
        visited[v] = True
    return mst

#CYKL EULERA
def euler_cycle(G):
    def dfs_visit(G, u):
        nonlocal cycle
        for neighbour in G[u]:
            G[u].remove(neighbour)
            G[neighbour].remove(u)
            dfs_visit(G, neighbour)
        cycle.append(u)
    n = len(G)
    cycle = []
    time = 0
    dfs_visit(G, 0)
    return cycle[::-1]

#MOSTY
def bridges(G):
    n = len(G)
    low = [0] * n
    times = [0] * n
    bridges = []
    time = 0
    def dfs(u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time
        for v in G[u]:
            if not times[v]:
                dfs(v, u)
                if low[v] < low[u]:
                    low[u] = low[v]
            elif v != parent:
                if times[v] < low[u]:
                    low[u] = times[v]
        if times[u] == low[u] and parent >= 0:
            bridges.append((parent, u))
    for i in range(n):
        if not times[i] :
            dfs(i, -1)
    return bridges

#SILNIE SPOJNE SKLADOWE
def dfs(G, s, result, visited):
    visited[s] = True
    for neighbour in G[s]:
        if visited[neighbour] is False:
            dfs(G, neighbour, result, visited)
    result.append(s)
    return visited, result

def reverse_edges(G):
    new_graph = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for j in G[i]:
            new_graph[j].append(i)
    return new_graph

def sss(G):
    n = len(G)
    visited = [False] * n
    stack = []
    stack = dfs(G, 0, stack, visited)[1]
    new_graph = reverse_edges(G)
    visited = [False] * n
    path = []

    while stack:
        vertex = stack.pop()
        if visited[vertex] is False:
            visited, path = dfs(new_graph, vertex, path, visited) 