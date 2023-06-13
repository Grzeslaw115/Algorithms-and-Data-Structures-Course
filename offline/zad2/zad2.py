'''Jakub Grzes
Maksymalna ilosc sniegu mozliwa do zebrania mozna znalezc poprzez wyznaczenie zbioru sektorow, ktore nalezy odwiedzic podczas pobierania sniegu. 
Dowolny podzbior sektorow jest osiagalny bez rozjezdzania jego elementow. 
Sortujac wartosci rosnaco po ilosci sniegu w sektorze do zmiennej collected bede dodawal kolejne najwieksze wartosci w tablicy, uwzgledniajac topnienie sniegu przy kazdym pojedynczym zbiorze. 
Procedure moge kontynuowac do napotkania 0, wowczas snieg w rozwazanym sektorze ulegl stopieniu, a skoro dane byly posortwane, wawoz musi byc pusty. 
Przez dobor najwiekszych elementow ilosc zebranego sniegu bedzie najwieksza z mozliwych. 
Celem usprawnienia algorytmu stosuje heap_sort_max, ktora przerywa sortowanie heap sort, gdy wartosc w korzeniu bedzie mniejsza lub rowna ilosci juz posortowanych elementow.
Tych i mniejszych wartosci nie warto sortowac, poniewaz z uwagi na topnienie, nie beda one uwzglednione w zbiorach.
'''

from zad2testy import runtests

def snow( S ):
    def heap_sort_max(A):
        def right(i):
            return 2 * i + 2
        def left(i):
            return 2 * i +1
        def parent(i):
            return (i-1) // 2

        def heapify(A, i, n):
            l = left(i)
            r = right(i)
            max_ind = i

            if l < n and A[l] > A[max_ind]:
                max_ind = l
            if r < n and A[r] > A[max_ind]:
                max_ind = r
            if max_ind != i:
                A[i], A[max_ind] = A[max_ind], A[i]
                heapify(A, max_ind, n)

        def build_heap(A): 
            n = len(A)
            for i in range(parent(n-1), -1, -1):
                heapify(A, i, n)

        n = len(A)
        build_heap(A)

        counter  = 0
        for i in range(n-1, 0, -1):
            if A[0] < counter:
                break
            A[0], A[i] = A[i], A[0]
            counter += 1
            heapify(A, 0, i)

        return A

    n = len(S)
    heap_sort_max(S)
    collected = 0
    days = 0

    while S[n - 1 - days] > 0:
        collected += S[n - 1 - days]
        S[n - 2 - days] -= days + 1 
        days += 1
        
    return collected

runtests( snow, all_tests = True )