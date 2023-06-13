from kol2testy import runtests
from queue import deque

def beautree(G):

    def is_consistent(edges, vertices):
        G = [[] for _ in range(vertices)]
        for edge in edges:
            G[edge[0]].append(edge[1])
            G[edge[1]].append(edge[0])
        def bfs(G):
            n = len(G)
            visited = [False] * n
            queue = deque()
            queue.append(0)
            visited[0] = True
            while queue:
                vertex = queue.popleft()
                for neighbour in G[vertex]:
                    if visited[neighbour] is False:
                        visited[neighbour] = True
                        queue.append(neighbour)
            for i in range(n):
                if visited[i] is False:
                    return False
            return True
        return bfs(G)
    
    def get_edges(G):
        n = len(G)
        edges = []
        for i in range(n):
            for edge in G[i]:
                if edge[0] > i:
                    edges.append((edge[0], i, edge[1]))
        edges.sort(key = lambda x: x[2])
        return edges

    def find_first_tree(edges, G):
        no_edges = len(edges)
        vertices = len(G)
        cost = 0
        for i in range(no_edges - vertices + 1):
            candidate = edges[i:i + vertices - 1]
            if is_consistent(candidate, vertices):
                for i in candidate:
                    cost += i[2]
                break
        if cost == 0:
            return None
        return cost

    edges = get_edges(G)
    return find_first_tree(edges, G)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )