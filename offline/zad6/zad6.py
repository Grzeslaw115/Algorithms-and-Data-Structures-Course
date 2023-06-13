'''Jakub Grzes
Traktuje zbior pracownikow i maszyn jako dwa niepolaczone wewnetrzenie zbiory grafu dwudzielnego. Buduje siec tworzac dodatkowe wierzcholki - zrodlo polaczone z pracownikami
i ujscie polaczone z maszynami. Uruchamiam alogorytm Forda-Fulkersona startujac ze zrodla i mierze przeplyw w ujsciu, przyznajac kazdej krawedzi pojemnosc 1. Otrzymany
wynik to rozmiar najwiekszego skojarzenia w grafie, zatem maksymalna liczba pracownikow pracuje jednoczesnie (na 1 maszynie maksymalnie 1 pracownik). 
Zlozonosc obliczeniowa algorytmu szacuje na O(V^3) gdzie V to liczba wierzcholkow.
'''

from zad6testy import runtests
from queue import deque

def binworker( M ):

    def build_network(G):
        n = len(G)
        for i in range(n):
            for j in range(len(G[i])):
                G[i][j] += n
            G.append([2*n+1])
        G.append([])
        for i in range(n):
            G[2*n].append(i)
        G.append([])
        return G
    
    def find_path(G, s, t):
        n = len(G)
        visited = [False] * n
        queue = deque()
        parent = [None] * n
        visited[s] = True
        queue.append(s)
        while len(queue) > 0:
            vertex = queue.pop()
            for neighbour in G[vertex]:
                if visited[neighbour] is False:
                    visited[neighbour] = True
                    parent[neighbour] = vertex
                    queue.append(neighbour)
            if visited[t] is True:
                break
            
        path = [t]
        vertex = t
        while parent[vertex] != None:
            path.append(parent[vertex])
            vertex = parent[vertex]
        if visited[t] is False:
            return None
        return path

    def ford_fulkerson(G, s, t):
        result = 0
        path = find_path(G, s, t)
        while path is not None:
            result += 1
            for i in range(len(path) - 1):
                G[path[i]].append(path[i + 1])
                G[path[i + 1]].remove(path[i])
            path = find_path(G, s, t)
        return result
        
    G = build_network(M)
    n = len(G)
    return ford_fulkerson(G, n - 2, n - 1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )