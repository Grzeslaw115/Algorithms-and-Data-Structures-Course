'''Jakub Grzes
Definiuje funkcje convert, ktora dla przyjetego slowa generuje jego odwrotnosc, a nastepnie tworzy slowo bedace "sklejeniem" zadanego slowa i jego odwrotnosci w kolejnosci alfabetycznej.
W ten sposob zapewniam jednoznaczna oraz unikalna reprezentacje wyrazow rownowaznych w tablicy. 
Nastepnie sortuje slowa alfabetycznie wymuszajac w ten sposob, aby te same wartosci znalazly sie "obok siebie" na kolejnych indeksach.
Przechodze po tablicy zliczajac dlugosc kazdego bloku zlozonego z tych samych wyrazow, pamietajac najdluzsza otrzymana dotychczas wartosc.
Zwracam dlugosc bloku dla ktorego nie istnial zaden szerszy. W ten sposob otrzymam poprawny rezultat dla dowolnego zestawu danych z zadania.
'''

from zad3testy import runtests

def strong_string(T):

    def merge_sort(T):
        if len(T) == 1:
            return T
        else:
            mid_pos = len(T) // 2
            L = T[mid_pos:]
            R = T[:mid_pos]
            merge_sort(L)
            merge_sort(R)

            l = r = q = 0

            while l < len(L) and r < len(R):
                if L[l] < R[r]:
                    T[q] = L[l]
                    l += 1
                else:
                    T[q] = R[r]
                    r += 1
                q += 1

            while l < len(L):
                T[q] = L[l]
                l += 1
                q += 1
            while r < len(R):
                T[q] = R[r]
                r += 1
                q += 1
            return T    


    def convert(word):
        reversed_word = word[::-1]
        result = ""
        if word < reversed_word:
            result = result + word + reversed_word
        else:
            result = result + reversed_word + word

        return result


    N = len(T)
    for i in range(N):
        T[i] = convert(T[i])

    merge_sort(T)
    i = 0
    counter = 1
    best_counter = 0
    while i < N - 1:
        if T[i] == T[i + 1]:
            counter += 1
        else:
            if counter > best_counter:
                best_counter = counter
            counter = 1
        i += 1
     
    return best_counter

runtests( strong_string, all_tests=True )
