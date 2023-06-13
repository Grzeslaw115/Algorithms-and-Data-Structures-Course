'''Jakub Grzes
Alogrytm ustala jedna sciezke o najkrotszej mozliwej dlugosci miedzy s i t uzywajac BFS, jesli jej nie ma, funkcja zwraca None. 
Nastepnie funkcja wyznacza nowy graf bedacy kopia grafu wejsciowego pozbawiona pojedynczej krawedzi ze znalezionej sciezki. 
Szuka w nim najkrotszej sciezki i jesli ta sie wydluzyla, zwraca usunieta krawedz, jesli nie, usuwa z nowej kopii kolejna krawedz sciezki i powtarza proces.
Jesli nie udalo sie zwrocic takiej krawedzi, funkcja zwraca None. Zlozonosc mojego algorytmu szacuje na O(E(V+E)) gdzie V to ilosc wierzchokow a E to ilosc krawedzie w G.
'''
from zad4testy import runtests
from collections import deque

def longer( G, s, t ):
    
    def find_shortest_path(G, s, t):
        visited = [False] * len(G)
        queue = deque()
        parent = [None] * len(G)

        visited[s] = True
        queue.append(s)

        while len(queue) > 0:
            vertex = queue.popleft()
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

    def delete_edge(G, s, t):
        G[s].remove(t)
        G[t].remove(s)
        return G
    
    path = find_shortest_path(G, s, t)
    if path is None:
        return None
    else:
        path_len_beginning = len(path)
        for i in range(len(path) - 1):
            ac_G = delete_edge(G, path[i], path[i+1])
            ac_path = find_shortest_path(ac_G, s, t)
            if ac_path is None:
                return (path[i], path[i+1])
            else:
                ac_path_len = len(ac_path)
            if ac_path_len > path_len_beginning:
                return (path[i], path[i+1])
    return None

runtests( longer, all_tests = True )