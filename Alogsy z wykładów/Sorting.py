def bubble_sort(tab):
    flag = False
    to_do = len(tab)

    while to_do > 1:
        flag = False
        for i in range(0, to_do-1):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = tab[i+1], tab[i]
                flag = True
        if not flag:
            break
        to_do -= 1
    return tab

def insertion_sort(tab):
    i = 1
    while i < len(tab):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
        i += 1
    return tab

def merge_sort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[mid:]
        R = tab[:mid]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0 

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1
        
    return tab

def heap_sort(A):
    def right(i):
        return 2 * i + 2
    def left(i):
        return 2 * i +1
    def parent(i):
        return (i-1) // 2
    
    def heapify(A, i, n): #zamieniam elemnt w "trojce" i patrze czy podmiana jest okej
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

    def build_heap(A): #buduje kopiec heapify po rodzicach najniższego poziomu
        n = len(A)

        for i in range(parent(n-1), -1, -1):
            heapify(A, i, n)

    n = len(A)
    build_heap(A)

    for i in range(n-1, 0, -1):  #wymieniam korzen z elementem ostatniego indeksu i heapify
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)

    return A

def quick_sort(A, p ,r):

    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i + 1

    while p < r:
        q = partition(A, p ,r)
        quick_sort(A, p, q-1)
        p = q + 1 #albo quicksort(A, q + 1, r)

    return A