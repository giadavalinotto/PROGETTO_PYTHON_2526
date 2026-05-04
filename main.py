from matrice import crea_matrice
from input_utils import chiedi_dimensione_matrice, leggi_coordinata
from algoritmi import bfs_lista, dfs_lista
from visualizzazione import stampa_percorso, visualizza_percorso


# MAIN
def main():
    while True:
        try:
            difficolta = int(input("Inserisci il livello di difficoltà (da 0 a 10): "))
            if 0 <= difficolta <= 10:
                prob_ostacolo = difficolta / 10
                break
            else:
                print("Il livello di difficoltà deve essere tra 0 e 10.")
        except ValueError:
            print("Inserisci un numero intero valido.")

    n = chiedi_dimensione_matrice() # chiedo all'utente la dimensione N della matrice
    matrice = crea_matrice(n, prob_ostacolo) # creo la matrice N x N con ostacoli generati casualmente in base alla probabilità specificata

    for riga in matrice:
        print(riga)

    # Chiedo all'utente le coordinate del punto di partenza
    start_row = leggi_coordinata(n, "Inserisci la riga del punto di partenza: ") # chiedo all'utente di inserire la riga del punto di partenza utilizzando la funzione leggi_coordinata, che assicura che l'input sia un numero intero valido compreso tra 0 e N-1
    start_col = leggi_coordinata(n, "Inserisci la colonna del punto di partenza: ") # chiedo all'utente di inserire la colonna del punto di partenza utilizzando la funzione leggi_coordinata, che assicura che l'input sia un numero intero valido compreso tra 0 e N-1
    start = (start_row, start_col) # creo una tupla start che contiene le coordinate del punto di partenza (riga, colonna)

    # Chiedo all'utente le coordinate del punto di arrivo
    while True: # ciclo infinito finché l'utente non inserisce un punto di arrivo diverso dal punto di partenza
        end_row = leggi_coordinata(n, "Inserisci la riga del punto di arrivo: ") # chiedo all'utente di inserire la riga del punto di arrivo utilizzando la funzione leggi_coordinata, che assicura che l'input sia un numero intero valido compreso tra 0 e N-1
        end_col = leggi_coordinata(n, "Inserisci la colonna del punto di arrivo: ") # chiedo all'utente di inserire la colonna del punto di arrivo utilizzando la funzione leggi_coordinata, che assicura che l'input sia un numero intero valido compreso tra 0 e N-1
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

    percorso = bfs_lista(matrice, start, end) # chiamo la funzione bfs_lista per eseguire la ricerca in ampiezza (BFS) utilizzando una lista come coda, passando la matrice, il punto di partenza e il punto di arrivo come argomenti, e memorizzo il risultato nella variabile percorso
    stampa_percorso(percorso, "BFS") # chiamo la funzione stampa_percorso per stampare il percorso trovato dalla BFS, passando il percorso e una stringa "BFS" per indicare che si tratta del percorso trovato dalla BFS
    visualizza_percorso(matrice, percorso, start, end, "BFS") # chiamo la funzione visualizza_percorso per visualizzare graficamente la matrice con il percorso trovato dalla BFS, passando la matrice, il percorso, il punto di partenza e il punto di arrivo come argomenti. La funzione utilizza Matplotlib per creare una rappresentazione visiva della matrice con il percorso trovato dalla BFS.

    percorso = dfs_lista(matrice, start, end) # chiamo la funzione dfs_lista per eseguire la ricerca in profondità (DFS) utilizzando una lista come pila, passando la matrice, il punto di partenza e il punto di arrivo come argomenti, e memorizzo il risultato nella variabile percorso
    stampa_percorso(percorso, "DFS") # chiamo la funzione stampa_percorso per stampare il percorso trovato dalla DFS, passando il percorso e una stringa "DFS" per indicare che si tratta del percorso trovato dalla DFS
    visualizza_percorso(matrice, percorso, start, end, "DFS")

if __name__ == "__main__": # good practise che rende il codice riutilizzabile come modulo
    main() # chiama la funzione main() per eseguire il programma quando viene eseguito direttamente, ma permette anche di importare le funzioni in altri moduli senza eseguire il codice principale.