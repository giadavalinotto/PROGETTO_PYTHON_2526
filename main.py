import random

prob_ostacolo = 0.3  # 30% di probabilità che una casella sia un ostacolo

while True: # ciclo infinito finché l'utente non inserisce un input valido
    try:
        N = int(input("Inserisci la dimensione N della matrice: ")) # l'utente inserisce la dimensione della matrice, che viene convertita in un intero
        if N <= 0: # se l'utente inserisce un numero non positivo, viene sollevata un'eccezione
            raise ValueError("Inserisci un numero intero positivo.") # raise solleva un'eccezione con un messaggio di errore personalizzato
        break # se l'input è valido, esco dal ciclo
    except ValueError: # se viene sollevata un'eccezione di tipo ValueError (ad esempio, se l'utente inserisce un valore non numerico o un numero negativo), viene stampato un messaggio di errore e il ciclo continua a chiedere un nuovo input
        print("Input non valido. Inserisci un numero intero positivo.")

matrice = []  # inizializzo la matrice vuota
prob_ostacolo = 0.3  # 30% di probabilità che una casella sia un ostacolo

for riga in range(N): # ciclo for per ogni riga della matrice
    riga_corrente = [] # inizializzo la riga corrente vuota
    for colonna in range(N): # ciclo for per ogni colonna della matrice
        if random.random() < prob_ostacolo: # se il numero casuale (tra 0 e 1) è inferiore alla probabilità di ostacolo
            riga_corrente.append(1)  # inserisco un ostacolo in questa posizione
        else:
            riga_corrente.append(0)  # la casella è libera
    matrice.append(riga_corrente) # aggiungo la riga corrente alla matrice

for riga in matrice:
    print(riga)

# Chiedo all'utente le coordinate del punto di partenza
start_row = int(input("Inserisci la riga del punto di partenza (0-9): ")) # l'utente inserisce la riga del punto di partenza, che viene convertita in un intero
start_col = int(input("Inserisci la colonna del punto di partenza (0-9): ")) # l'utente inserisce la colonna del punto di partenza, che viene convertita in un intero
start = (start_row, start_col) # creo una tupla con le coordinate del punto di partenza

# Chiedi all'utente le coordinate del punto di arrivo
end_row = int(input("Inserisci la riga del punto di arrivo (0-9): ")) # l'utente inserisce la riga del punto di arrivo, che viene convertita in un intero
end_col = int(input("Inserisci la colonna del punto di arrivo (0-9): ")) # l'utente inserisce la colonna del punto di arrivo, che viene convertita in un intero
end = (end_row, end_col) # creo una tupla con le coordinate del punto di arrivo

# Imposto i valori nella matrice
matrice[start[0]][start[1]] = 0 # imposto il punto di partenza come libero (0) nella matrice
matrice[end[0]][end[1]] = 0 # imposto il punto di arrivo come libero (0) nella matrice

# Stampa per verificare
for riga in matrice:
    print(riga)

    #TODO implementare il controllo per verificare che le coordinate inserite siano valide (che non siano fuori dai limiti della matrice o che l'input non sia un numero) --> sotto forma di funzione
    #TODO controllare se parti di codice possono diventare delle funzioni per rendere il codice più modulare e leggibile (ad esempio, la generazione della matrice, la stampa della matrice, la validazione dell'input)