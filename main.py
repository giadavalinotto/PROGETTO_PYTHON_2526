# LIBRERIE
import random

# FUNZIONI
def chiedi_dimensione_matrice():
    while True:
        try:
            N = int(input("Inserisci la dimensione N della matrice: "))
            if N > 0:
                return N
            else:
                print("Inserisci un numero intero positivo.")
        except ValueError:
            print("Input non valido. Inserisci un numero intero positivo.")
    return N

def crea_matrice(N, prob_ostacolo):
    matrice = []  # inizializzo la matrice vuota
    for riga in range(N):  # ciclo for per ogni riga della matrice
        riga_corrente = []  # inizializzo la riga corrente vuota
        for colonna in range(N):  # ciclo for per ogni colonna della matrice
            if random.random() < prob_ostacolo:  # se il numero casuale (tra 0 e 1) è inferiore alla probabilità di ostacolo
                riga_corrente.append(1)  # inserisco un ostacolo in questa posizione
            else:
                riga_corrente.append(0)  # la casella è libera
        matrice.append(riga_corrente)  # aggiungo la riga corrente alla matrice
    return matrice  # restituisco la matrice generata

def leggi_coordinata(N, messaggio):
    while True:
        try:
            valore = int(input(messaggio))
            if 0 <= valore < N:
                return valore
            else:
                print("Inserisci un numero compreso tra 0 e " + str(N-1))
        except ValueError:
            print("Inserisci un numero intero valido")

# MAIN
prob_ostacolo = 0.3  # 30% di probabilità che una casella sia un ostacolo

N = chiedi_dimensione_matrice()
matrice = crea_matrice(N, prob_ostacolo)

for riga in matrice:
    print(riga)

# Chiedo all'utente le coordinate del punto di partenza
start_row = leggi_coordinata(N, "Inserisci la riga del punto di partenza: ")
start_col = leggi_coordinata(N, "Inserisci la colonna del punto di partenza: ")
start = (start_row, start_col)

# Chiedo all'utente le coordinate del punto di arrivo
while True:
    end_row = leggi_coordinata(N, "Inserisci la riga del punto di arrivo: ")
    end_col = leggi_coordinata(N, "Inserisci la colonna del punto di arrivo: ")
    end = (end_row, end_col)

    if end != start:
        break
    else:
        print("Il punto di arrivo non può coincidere con il punto di partenza.")

# Imposto i valori nella matrice
matrice[start[0]][start[1]] = 0 # imposto il punto di partenza come libero (0) nella matrice
matrice[end[0]][end[1]] = 0 # imposto il punto di arrivo come libero (0) nella matrice

# Stampa per verificare
for riga in matrice:
    print(riga)