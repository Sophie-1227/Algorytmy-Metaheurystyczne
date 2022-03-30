#Algorytm najblizszego sasiada
import random as rand
"""
Opisowo:
1. Losujemy punkt rozpoczęcie trasy (możemy też go wybrać na twardo i też będzie dobrze) i dodajemy go na początek listy pi (listy kolejnych odwiedzanych punktów.
2. Dla tego punktu szukamy w matrixie najmniejszej odleglości do dowolnego innego punktu (NALEŻY SPRAWDZIĆ CZY WYBRANY PUNKT NIE JEST POCZĄTKOWYM LUB SAMYM SOBĄ)
3. Dodajemy długość tej trasy do sumarycznej odległości, a numer punkty do listy pi
4. I Powtarzamy punkty 2 i 3
5. Wykreślamy poprzedni punkt z dostępnych do losowania
6. Kiedy zostaną nam ostatnie 2 punkty To ta trasa musi być do punktu początkowego, dodajemy odległość, ale punkty do pi juz nie musimy
7. Wyświetlamy i się cieszymy jak działa
"""

"""
Pseudokod:
s = random od 1 do 29 # punkt startowy
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
print(odleglosc)
print(list)     
"""

def NN_algo(problem, k):
    if k==0 :
        starting = rand.randint(1,29)
    else:
        starting = k
    dimension = problem.dimension
    endList = []
        #list(range(1, dimension + 1))
    odleglosc = 0
    point = starting
    endList.append(starting)

    for i in range (1,dimension):
        best = 927638108236
        for j in range (1,30-len(endList)):
            temp = problem.get_weight(*(endList[-1], j))
            if temp < best and j not in endList:
                best = temp
                point = j
        endList.append(point)
        #print("przed ", best, "iteracja ", i)
        odleglosc += best
        #print("odleglosc 1 ", odleglosc)
    odleglosc += problem.get_weight(*(endList[-1], starting))

    print(odleglosc)
    print(endList)
    return odleglosc, endList[0]
