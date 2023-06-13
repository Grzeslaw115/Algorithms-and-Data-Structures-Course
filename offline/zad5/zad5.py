''' Jakub Grzes
Znajde czas nakrotszej sciezki obliczajac czas przelotu z a do b nie korzystajac z osobliwosci, a nastepnie znajde minimalne czasy dojscia do najblizszej osobliwosci z a i z b.
Wiem, ze najkrotszy czas zawarty bedzie w ktorejs z tych dwoch zmiennych, bowiem jesli sciezka nie przebiega przez zadna osobliwosc, zostanie ona zapisana w pierwszej zmiennej,
a w przeciwnym przypadku, jej dlugosc wyrazi sie przez najkrotszy dojscia do zbioru wierzcholkow z osobliwosci (daze do uzycia jej w taki sposob, aby maksymalnie skrocic droge z a do b,
wiec nie warto rozwazac osobno przelotow miedzy osobliwosciami, ktore nie wplyna na optymalny czas przelotu, t.j. dojscia do najblizszych osobliwosci). 
Oblicze je uruchamiajac algorytm Dijkstry osobno z a i z b.
Jesli obie wartosci wyniosa nieskonczonosc, b jest nieosiagalne z a i funkcja zwroci None. W przeciwnym przypadku zwroce mniejsza z tych wartosci.
Zlozonosc obliczeniowa szacuje na O(S + E*log(V)), gdzie S to moc zbioru osobliwosci, E to liczba krawedzi, a V to liczba wierzcholkow.
'''
from zad5testy import runtests
from queue import PriorityQueue

def spacetravel( n, E, S, a, b):
    def convert_graph(E, n):
        graph = [[] for _ in range(n)]
        for i in range(len(E)):
            edge = E[i]
            graph[edge[0]].append((edge[1], edge[2]))
            graph[edge[1]].append((edge[0], edge[2]))
        return graph

    E = convert_graph(E, n)

    time_a = [float('inf')] * n
    time_a[a] = 0
    visited = [False] * n
    queue = PriorityQueue()
    queue.put((0, a))

    while queue.empty() is False:
        vertex = queue.get()[1]
        if visited[vertex] is True:
            continue
        for neighbour in E[vertex]:
            if time_a[neighbour[0]] > time_a[vertex] + neighbour[1]:
                time_a[neighbour[0]] = time_a[vertex] + neighbour[1]
                queue.put((time_a[vertex] + neighbour[1], neighbour[0]))
        visited[vertex] = True
    no_teleport = time_a[b]

    time_b = [float('inf')] * n
    time_b[b] = 0
    visited = [False] * n
    queue = PriorityQueue()
    queue.put((0, b))

    while queue.empty() is False:
        vertex = queue.get()[1]
        if visited[vertex] is True:
            continue
        for neighbour in E[vertex]:
            if time_b[neighbour[0]] > time_b[vertex] + neighbour[1]:
                time_b[neighbour[0]] = time_b[vertex] + neighbour[1]
                queue.put((time_b[vertex] + neighbour[1], neighbour[0]))
        visited[vertex] = True

    min_from_a = float('inf')
    min_from_b = float('inf')
    for i in range(len(S)):
        if min_from_a > time_a[S[i]]:
            min_from_a = time_a[S[i]]
        if min_from_b > time_b[S[i]]:
            min_from_b = time_b[S[i]]
    teleport = min_from_a + min_from_b
    to_return = min(teleport, no_teleport)
    if to_return == float('inf'):
        return None
    return to_return
runtests( spacetravel, all_tests = False )