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

def NN_algo():
    starting = random.randint(1,29)