import random

def crea_matrice(n, prob_ostacolo):
    matrice = []
    for riga in range(n):
        riga_corrente = []
        for colonna in range(n):
            if random.random() < prob_ostacolo:  # se il numero casuale (tra 0 e 1) generato è inferiore alla probabilità di ostacolo
                riga_corrente.append(1)
            else:
                riga_corrente.append(0)
        matrice.append(riga_corrente)
    return matrice