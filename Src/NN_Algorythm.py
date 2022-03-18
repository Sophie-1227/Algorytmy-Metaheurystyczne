#Algorytm najblizszego sasiada
from random import random
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

def NN_algo():
    starting = random.randint(1,29)
    endList = []
    odleglosc = 0
    endList.append(starting)
    for i in range (29):
        best = 927638108236
        for j in range (29):
            temp = matrix[i][j] #nie mam pojęcia jak wejsc do tego matrixa, bo potrzebuje wyciagnac konkretna wartosc odleglosci
            if temp<best and j not in endList:
                best = temp
                point = j
        endList.append(point)
        odleglosc += best
    odleglosc += matrix[point][starting]
print(odleglosc)
print(endList)




