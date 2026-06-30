def chiedi_dimensione_matrice():
    while True: # ciclo infinito finché l'utente non inserisce un numero intero positivo valido
        try:
            n = int(input("Inserisci la dimensione N della matrice: "))
            if n > 0:
                return n
            else: # se N non è un numero intero positivo
                print("Inserisci un numero intero positivo.")
        except ValueError: # se l'utente inserisce un input che non può essere convertito in un intero
            print("Input non valido. Inserisci un numero intero positivo.")


def leggi_coordinata(n, messaggio):
    while True: # ciclo infinito finché l'utente non inserisce un numero intero valido compreso tra 0 e N-1
        try:
            valore = int(input(messaggio))
            if 0 <= valore < n:
                return valore
            else:
                print("Inserisci un numero compreso tra 0 e " + str(n-1))
        except ValueError: # se l'utente inserisce un input che non può essere convertito in un intero
            print("Inserisci un numero intero valido")
