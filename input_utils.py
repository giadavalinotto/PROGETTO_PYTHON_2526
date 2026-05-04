def chiedi_dimensione_matrice(): # funzione per chiedere all'utente la dimensione N della matrice
    while True: # ciclo infinito finché l'utente non inserisce un numero intero positivo valido
        try: # provo a convertire l'input dell'utente in un intero
            n = int(input("Inserisci la dimensione N della matrice: ")) # chiedo all'utente di inserire la dimensione N della matrice
            if n > 0: # se N è un numero intero positivo, lo restituisco
                return n # restituisco la dimensione N della matrice
            else: # se N non è un numero intero positivo, stampo un messaggio di errore e continuo a chiedere
                print("Inserisci un numero intero positivo.") # stampo un messaggio di errore se l'utente inserisce un numero non positivo
        except ValueError: # se l'utente inserisce un input che non può essere convertito in un intero, stampo un messaggio di errore e continuo a chiedere
            print("Input non valido. Inserisci un numero intero positivo.") # stampo un messaggio di errore se l'utente inserisce un input non valido (ad esempio, una stringa o un numero decimale)


def leggi_coordinata(n, messaggio): # funzione per leggere una coordinata (riga o colonna) dall'utente, assicurandosi che sia un numero intero valido compreso tra 0 e N-1
    while True: # ciclo infinito finché l'utente non inserisce un numero intero valido compreso tra 0 e N-1
        try: # provo a convertire l'input dell'utente in un intero
            valore = int(input(messaggio)) # chiedo all'utente di inserire una coordinata (riga o colonna) utilizzando il messaggio specificato
            if 0 <= valore < n: # se il valore è un numero intero valido compreso tra 0 e N-1, lo restituisco
                return valore # restituisco la coordinata inserita dall'utente
            else: # se il valore non è un numero intero valido compreso tra 0 e N-1, stampo un messaggio di errore e continuo a chiedere
                print("Inserisci un numero compreso tra 0 e " + str(n-1)) # stampo un messaggio di errore se l'utente inserisce un numero fuori dal range valido
        except ValueError: # se l'utente inserisce un input che non può essere convertito in un intero, stampo un messaggio di errore e continuo a chiedere
            print("Inserisci un numero intero valido") # stampo un messaggio di errore se l'utente inserisce un input non valido (ad esempio, una stringa o un numero decimale)
