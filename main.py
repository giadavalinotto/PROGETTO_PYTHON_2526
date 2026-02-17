# LIBRERIE
import random

# FUNZIONI
def chiedi_dimensione_matrice(): # funzione per chiedere all'utente la dimensione N della matrice
    while True: # ciclo infinito finché l'utente non inserisce un numero intero positivo valido
        try: # provo a convertire l'input dell'utente in un intero
            N = int(input("Inserisci la dimensione N della matrice: ")) # chiedo all'utente di inserire la dimensione N della matrice
            if N > 0: # se N è un numero intero positivo, lo restituisco
                return N # restituisco la dimensione N della matrice
            else: # se N non è un numero intero positivo, stampo un messaggio di errore e continuo a chiedere
                print("Inserisci un numero intero positivo.") # stampo un messaggio di errore se l'utente inserisce un numero non positivo
        except ValueError: # se l'utente inserisce un input che non può essere convertito in un intero, stampo un messaggio di errore e continuo a chiedere
            print("Input non valido. Inserisci un numero intero positivo.") # stampo un messaggio di errore se l'utente inserisce un input non valido (ad esempio, una stringa o un numero decimale)
    return N

def crea_matrice(N, prob_ostacolo): # funzione per creare una matrice N x N con ostacoli generati casualmente in base alla probabilità specificata
    matrice = []  # inizializzo la matrice vuota
    for riga in range(N):  # ciclo for per ogni riga della matrice
        riga_corrente = []  # inizializzo la riga corrente vuota
        for colonna in range(N):  # ciclo for per ogni colonna della matrice
            if random.random() < prob_ostacolo:  # se il numero casuale (tra 0 e 1) è inferiore alla probabilità di ostacolo
                riga_corrente.append(1)  # inserisco un ostacolo in questa posizione
            else: # altrimenti, se il numero casuale è maggiore o uguale alla probabilità di ostacolo
                riga_corrente.append(0)  # la casella è libera
        matrice.append(riga_corrente)  # aggiungo la riga corrente alla matrice
    return matrice  # restituisco la matrice generata

def leggi_coordinata(N, messaggio): # funzione per leggere una coordinata (riga o colonna) dall'utente, assicurandosi che sia un numero intero valido compreso tra 0 e N-1
    while True: # ciclo infinito finché l'utente non inserisce un numero intero valido compreso tra 0 e N-1
        try: # provo a convertire l'input dell'utente in un intero
            valore = int(input(messaggio)) # chiedo all'utente di inserire una coordinata (riga o colonna) utilizzando il messaggio specificato
            if 0 <= valore < N: # se il valore è un numero intero valido compreso tra 0 e N-1, lo restituisco
                return valore # restituisco la coordinata inserita dall'utente
            else: # se il valore non è un numero intero valido compreso tra 0 e N-1, stampo un messaggio di errore e continuo a chiedere
                print("Inserisci un numero compreso tra 0 e " + str(N-1)) # stampo un messaggio di errore se l'utente inserisce un numero fuori dal range valido
        except ValueError: # se l'utente inserisce un input che non può essere convertito in un intero, stampo un messaggio di errore e continuo a chiedere
            print("Inserisci un numero intero valido") # stampo un messaggio di errore se l'utente inserisce un input non valido (ad esempio, una stringa o un numero decimale)

# MAIN
prob_ostacolo = 0.3  # 30% di probabilità che una casella sia un ostacolo

N = chiedi_dimensione_matrice() # chiedo all'utente la dimensione N della matrice
matrice = crea_matrice(N, prob_ostacolo) # creo la matrice N x N con ostacoli generati casualmente in base alla probabilità specificata

#for riga in matrice:
#    print(riga)

# Chiedo all'utente le coordinate del punto di partenza
start_row = leggi_coordinata(N, "Inserisci la riga del punto di partenza: ") # chiedo all'utente di inserire la riga del punto di partenza utilizzando la funzione leggi_coordinata, che assicura che l'input sia un numero intero valido compreso tra 0 e N-1
start_col = leggi_coordinata(N, "Inserisci la colonna del punto di partenza: ") # chiedo all'utente di inserire la colonna del punto di partenza utilizzando la funzione leggi_coordinata, che assicura che l'input sia un numero intero valido compreso tra 0 e N-1
start = (start_row, start_col) # creo una tupla start che contiene le coordinate del punto di partenza (riga, colonna)

# Chiedo all'utente le coordinate del punto di arrivo
while True: # ciclo infinito finché l'utente non inserisce un punto di arrivo diverso dal punto di partenza
    end_row = leggi_coordinata(N, "Inserisci la riga del punto di arrivo: ") # chiedo all'utente di inserire la riga del punto di arrivo utilizzando la funzione leggi_coordinata, che assicura che l'input sia un numero intero valido compreso tra 0 e N-1
    end_col = leggi_coordinata(N, "Inserisci la colonna del punto di arrivo: ") # chiedo all'utente di inserire la colonna del punto di arrivo utilizzando la funzione leggi_coordinata, che assicura che l'input sia un numero intero valido compreso tra 0 e N-1
    end = (end_row, end_col) # creo una tupla end che contiene le coordinate del punto di arrivo (riga, colonna)
    if end != start: # se il punto di arrivo è diverso dal punto di partenza, esco dal ciclo
        break # altrimenti, se il punto di arrivo coincide con il punto di partenza, stampo un messaggio di errore e continuo a chiedere
    else: # se il punto di arrivo coincide con il punto di partenza, stampo un messaggio di errore e continuo a chiedere
        print("Il punto di arrivo non può coincidere con il punto di partenza.") # stampo un messaggio di errore se l'utente inserisce un punto di arrivo che coincide con il punto di partenza

# Imposto i valori nella matrice
matrice[start[0]][start[1]] = 0 # imposto il punto di partenza come libero (0) nella matrice
matrice[end[0]][end[1]] = 0 # imposto il punto di arrivo come libero (0) nella matrice

# Stampa per verificare
for riga in matrice: # ciclo for per ogni riga della matrice
    print(riga) # stampo la matrice per verificare che i punti di partenza e arrivo siano stati impostati correttamente come liberi (0) e che gli ostacoli siano stati generati casualmente in base alla probabilità specificata