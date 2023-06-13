'''Jakub Grzes
Algorytm dla kazdego indeksu 'z' wyznacza tablice arr bedaca kopia tablicy wejsciowej w przedziale indeksow [indeks_z, indeks_z + p - 1].
Dla kazdej takiej tablicy wyznaczam (len(arr) - k)-ta statystyke pozycyjna, t.j. k-ta najwieksza wartosc, po czym dodaje ja do zmiennej result.
Po wykonywaniu petli do momentu gdy indeks 'z' bedzie rowny n-p, zwracam wynik. Zlozonosc obliczeniowa mojego algorytmu szacuje na O(np), gdzie n jest liczba elementow
w tablicy, a p to liczba elementow w przedzialach w ktorych elementy sa sumowane.
'''

from kol1testy import runtests

def ksum(T, k, p):

    def select(A, k):
        def partition(A, p, r):
            x = A[r]
            i = p - 1
            for j in range(p, r):
                if A[j] <= x:
                    i += 1
                    A[i], A[j] = A[j], A[i]
            A[i+1], A[r] = A[r], A[i+1]
            return i + 1
        p = 0
        r = len(A) - 1
        while p <= r:
            q = partition(A, p, r) 
            if q == k:
                return A[q]
            if q < k:
                p = q + 1
            else:
                r = q - 1
        return None

    result = 0 
    N = len(T)
    z_index = 0
    while z_index <= N-p:
        arr = T[z_index:(z_index + p)]
        result += select(arr, len(arr) - k)
        z_index += 1

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )