'''
Jakub Grzes

Szukany palindrom ma byc nieparzystej dlugosci, wiec moge go potraktowac jak slowo o takiej wlasnosci, ze ma "srodek" w polowie swojej dlugosci i dla 
kazdego x z przedzialu [0, (dlugosc_slowa) // 2] slowo[srodek - x] == slowo[srodek + x].
Kazda litere w slowie traktuje jak potencjalny srodek dla ktorego sprawadzam powyzsza wlasnosc pilnujac, aby nie wykroczyc poza zakres slowa.
Jesli dla danej litery ustalam dluzszy palindrom niz wczesniej znaleziony, przypisuje jego dlugosc do zmiennej max_len.
Dla danego srodka maksymalna mozliwa dlugosc palindromu to 2*(dlugosc_slowa - indeks_srodka - 1) + 1 z uwagi na dlugosc zadanego slowa, wiec wlasnosc sprawdzam tylko dla takich srodkow, 
gdzie mozliwe jest uzyskanie palindromu dluzszego niz ten, ktorego dlugosc jest juz w zmiennej max_len.
Wykonanie algorytmu oznacza rozwazenie wszystkich istotnych mozliwosci, wiec funkcja zwroci poprawne dane dla dowolnego slowa s.
Zloznosc obliczeniowa szacuje na O(n^2).
'''

from zad1testy import runtests

def ceasar( s ):
    max_len = 1 
    s_len = len(s)
    ac_pos = 1

    while (s_len - ac_pos - 1) * 2 + 1 > max_len:
        i = 1
        ac_len = 1

        while ac_pos - i >= 0 and ac_pos + i < s_len and s[ac_pos + i] == s[ac_pos - i]:
            ac_len += 2
            i += 1
        if ac_len > max_len:
            max_len = ac_len
        ac_pos += 1

    return max_len

runtests( ceasar , all_tests = True )