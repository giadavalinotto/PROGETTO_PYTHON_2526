import random

def crea_matrice(n, prob_ostacolo): # funzione per creare una matrice N x N con ostacoli generati casualmente in base alla probabilità specificata
    matrice = []  # inizializzo la matrice vuota
    for riga in range(n):  # ciclo for per ogni riga della matrice
        riga_corrente = []  # inizializzo la riga corrente vuota
        for colonna in range(n):  # ciclo for per ogni colonna della matrice
            if random.random() < prob_ostacolo:  # se il numero casuale (tra 0 e 1) è inferiore alla probabilità di ostacolo
                riga_corrente.append(1)  # inserisco un ostacolo in questa posizione
            else: # altrimenti, se il numero casuale è maggiore o uguale alla probabilità di ostacolo
                riga_corrente.append(0)  # la casella è libera
        matrice.append(riga_corrente)  # aggiungo la riga corrente alla matrice
    return matrice  # restituisco la matrice generata