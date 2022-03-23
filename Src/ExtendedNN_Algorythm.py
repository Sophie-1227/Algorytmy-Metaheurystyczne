#mTak samo jak NNA tylko dodatkowa pętla pozwalająca rozpocząć od każdego z punktów, ale idk czy to legalne
import random as rand
"""
Opisowo:
1. Bierzemy po kolei każdy z punktów na mapie i dodajemy go na początek listy pi (listy kolejnych odwiedzanych punktów).
2. Dla tego punktu szukamy w matrixie najmniejszej odleglości do dowolnego innego punktu (NALEŻY SPRAWDZIĆ CZY WYBRANY PUNKT NIE JEST POCZĄTKOWYM LUB SAMYM SOBĄ)
3. Dodajemy długość tej trasy do sumarycznej odległości, a numer punkty do listy pi
4. I Powtarzamy punkty 2 i 3
5. Wykreślamy poprzedni punkt z dostępnych do losowania
6. Kiedy zostaną nam ostatnie 2 punkty To ta trasa musi być do punktu początkowego, dodajemy odległość, ale punkty do pi juz nie musimy
7. Wyświetlamy i się cieszymy jak działa
"""

"""
Pseudokod:

endResult = 938392818236392   
endList = []
for i in range (29):
    s = i # punkt startowy
    list.push(s)
    odleglosc = 0
    for i<-0 to 29 do
        best = 8364273 #duża odległość, żeby nie było problemu
        for j<-0 to 29 do
            temp = matrix[i][j]
            if temp<best && j nie należy do list
                best = temp
                point = j #punkt, uznany za najlepszy
            list.push(point)
            odleglosc += best
        odleglosc += matrix[j][s]
    if best<endResult
        endResult = best
        endList = list #przypisanie listy najlepszej do listy koncowej (zamieniamy wszystkie wartosci listy)
    print(endResult)
    print(endlist)
    

"""

def ENN_algo(problem):
    dimension = problem.dimension
    endList = []
    odleglosc = 0

    endResult = 927638108236
    for k in range(1, dimension):
        point = k
        list.append(point)
        for i in range (1,dimension):
            best = 927638108236
            for j in range (1,30):
                #temp = matrix[i][j] #nie mam pojęcia jak wejsc do tego matrixa, bo potrzebuje wyciagnac konkretna wartosc odleglosci
                temp = problem.get_weight(*(point, j))
                if temp < best and j not in endList:
                    best = temp
                    point = j
            list.append(point)
            #print("przed ", best, "iteracja ", i)
            odleglosc += best
            #print("odleglosc 1 ", odleglosc)
        odleglosc += problem.get_weight(*(point, k))
        if odleglosc < endResult:
            endResult = odleglosc
            endList = list  # przypisanie listy najlepszej do listy koncowej (zamieniamy wszystkie wartosci listy)

    print(endResult)
    print(endList)