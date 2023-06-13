'''Jakub Grzes
Zdefiniuje f(i, j) jako najwieksza ilosc komnat mozliwych do odwiedzenia konczacych sie na polu i, j. W obrebie danej kolumny moge wykonac jedynie szereg ruchow w dol
lub w gore (bo nie moge wracac sie na poprzednie pole) lub przejsc w prawo do nastepnej kolumny. f(i, j) = max(f(i-1,j), f(i,j-1), f(i,j+1)) + 1. 
Dla kazdej kolumny zadam osobno ruch w gore i w dol i oblicze szacunkowa wartosc f(i, j) ze wzgledu na ruch w danej kolumnie bazujac na wartosciach przepisanych z poprzedniej kolumny.
Do nastepnej kolumny przepisuje maksymalna otrzymana wartosc + 1 (ruch w prawo). Powtorze czynnosc dla kazdej kolumny pomijajac komnaty niedostepne i zwroce f(n-1, n-1) gdzie n to dlugosc L. 
Zlozonosc obliczeniowa algorytmu szacuje na O(n^2).
'''
from zad7testy import runtests

def maze( L ):
    n = len(L)
    matrix = [[[-float('inf'), -float('inf'), -float('inf')] for _ in range(n)] for _ in range(n)]
    for i in range(3):
        matrix[0][0][i] = 0

    def count_column(L, matrix, column):
        n = len(L)
        row = n - 1
        if column != 0:
            while row > 0:
                if L[row - 1][column] == '.':
                    if matrix[row - 1][column][1] < matrix[row][column][1] + 1:
                        matrix[row - 1][column][1] = matrix[row][column][1] + 1
                row -= 1
    
        row = 0
        while row < n-1:
            if L[row + 1][column] == '.':
                if matrix[row + 1][column][2] < matrix[row][column][2] + 1:
                    matrix[row + 1][column][2] = matrix[row][column][2] + 1
            row += 1

        if column < n-1:
            for i in range(n):
                if L[i][column + 1] == '.':
                    right = max(matrix[i][column]) + 1
                    for j in range(3):
                        matrix[i][column + 1][j] = right
        return matrix
        

    for i in range(n):
        count_column(L, matrix, i)
    to_return = max(matrix[n - 1][n - 1])
    if to_return == -float('inf'):
        return -1
    return to_return

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )