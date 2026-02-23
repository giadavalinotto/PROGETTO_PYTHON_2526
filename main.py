# LIBRERIE
import random # importo la libreria random per generare numeri casuali, che sarà utilizzata per creare la matrice con ostacoli generati casualmente in base alla probabilità specificata
import matplotlib.pyplot as plt # importo la libreria matplotlib.pyplot per visualizzare graficamente la matrice con il percorso trovato
import numpy as np # importo la libreria numpy per manipolare array e matrici, utilizzando l'alias np per semplificare la sintassi


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


def bfs_lista(matrice, start, end): # funzione per eseguire la ricerca in ampiezza (BFS) utilizzando una lista come coda, per trovare un percorso da start a end
    N = len(matrice) # ottengo la dimensione della matrice
    movimenti = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)] # lista dei movimenti possibili (8 direzioni: su, giù, sinistra, destra e diagonali)
    coda = [start]  # lista che funge da coda per la BFS, inizialmente contiene solo il nodo di partenza
    visitati = [start]  # lista dei nodi già visitati, inizialmente contiene solo il nodo di partenza
    predecessore = {}  # dizionario per tenere traccia del predecessore di ogni nodo visitato per ricostruire il percorso alla fine

    while coda: # finché la coda non è vuota
        nodo_corrente = coda.pop(0)  # prendo il primo nodo dalla coda (FIFO)
        if nodo_corrente == end:  # se il nodo corrente è il nodo di arrivo, ricostruisco il percorso usando il dizionario dei predecessori
            percorso = [] # lista per memorizzare il percorso trovato
            while nodo_corrente != start: # finché il nodo corrente non è il nodo di partenza, aggiungo il nodo corrente al percorso e aggiorno il nodo corrente al suo predecessore
                percorso.append(nodo_corrente) # aggiungo il nodo corrente al percorso
                nodo_corrente = predecessore[nodo_corrente] # aggiorno il nodo corrente al suo predecessore
            percorso.append(start) # aggiungo il nodo di partenza al percorso
            percorso.reverse() # inverto il percorso per avere l'ordine corretto da start a end
            return percorso # restituisco il percorso trovato

        riga, col = nodo_corrente # scompongo il nodo corrente nelle sue coordinate (riga e colonna)
        for dr, dc in movimenti: # ciclo for per ogni possibile movimento (dr, dc) nella lista dei movimenti
            nuova_riga = riga + dr # calcolo la nuova riga dopo aver applicato il movimento dr al nodo corrente
            nuova_col = col + dc # calcolo la nuova colonna dopo aver applicato il movimento dc al nodo corrente
            nuovo_nodo = (nuova_riga, nuova_col) # creo una tupla nuovo_nodo che rappresenta le coordinate del nuovo nodo dopo aver applicato il movimento al nodo corrente
            if 0 <= nuova_riga < N and 0 <= nuova_col < N: # se le nuove coordinate sono valide (cioè all'interno dei limiti della matrice)
                if matrice[nuova_riga][nuova_col] == 0 and nuovo_nodo not in visitati: # se la casella corrispondente al nuovo nodo è libera (0) e il nuovo nodo non è già stato visitato
                    coda.append(nuovo_nodo) # aggiungo il nuovo nodo alla coda per essere visitato in futuro
                    visitati.append(nuovo_nodo) # aggiungo il nuovo nodo alla lista dei nodi visitati per evitare di visitarlo nuovamente in futuro
                    predecessore[nuovo_nodo] = nodo_corrente # aggiorno il dizionario dei predecessori per indicare che il predecessore del nuovo nodo è il nodo corrente per poter ricostruire il percorso alla fine

    return None  # se la coda si svuota senza trovare il nodo di arrivo, restituisco None per indicare che non esiste un percorso da start a end

def visualizza_percorso(matrice, percorso, start, end):

    N = len(matrice) # ottengo la dimensione della matrice
    array = np.array(matrice) # converto la matrice in un array numpy per facilitare la manipolazione e la visualizzazione grafica

    # Creo un array RGB per i colori
    colori = np.zeros((N, N, 3)) # inizializzo un array di zeri con dimensioni (N, N, 3) per rappresentare i colori RGB di ogni cella della matrice, dove N è la dimensione della matrice e 3 rappresenta i canali di colore (rosso, verde, blu)
    for r in range(N): # ciclo for per ogni riga della matrice
        for c in range(N): # ciclo for per ogni colonna della matrice
            if array[r, c] == 1: # se la cella corrispondente alla posizione (r, c) è un ostacolo (1)
                colori[r, c] = [0, 0, 0]      # nero = ostacolo
            else: # se la cella corrispondente alla posizione (r, c) è libera (0)
                colori[r, c] = [1, 1, 1]      # bianco = cella libera

    # Evidenzio il percorso in lilla
    if percorso: # se esiste un percorso valido (cioè percorso non è None), evidenzio le celle del percorso in lilla
        for r, c in percorso: # ciclo for per ogni coppia di coordinate (r, c) nel percorso trovato
            if (r, c) != start and (r, c) != end: # se la cella del percorso non è il punto di partenza e non è il punto di arrivo, evidenzio la cella del percorso in lilla
                colori[r, c] = [0.8, 0.6, 1]  # lilla = percorso

    # Evidenzio start e end in viola
    colori[start[0], start[1]] = [0.6, 0, 0.6]  # viola = start
    colori[end[0], end[1]] = [0.6, 0, 0.6]      # viola = end

    # Visualizzazione
    plt.figure(figsize=(8,8)) # creo una figura di dimensioni 8x8 pollici per visualizzare la matrice con il percorso trovato
    plt.imshow(colori, origin='upper') # visualizzo l'array dei colori utilizzando la funzione imshow di Matplotlib, con l'origine in alto a sinistra (origin='upper') per far corrispondere le coordinate della matrice alla visualizzazione grafica

    # Griglia e dettagli estetici
    plt.xticks(range(N)) # imposto i tick dell'asse x per mostrare le coordinate delle colonne da 0 a N-1
    plt.yticks(range(N)) # imposto i tick dell'asse y per mostrare le coordinate delle righe da 0 a N-1
    plt.grid(color='gray', linestyle='-', linewidth=1) # aggiungo una griglia grigia con linee continue e spessore di 1 per migliorare la visibilità delle celle nella matrice
    plt.title("Percorso trovato", fontsize=16) # aggiungo un titolo alla visualizzazione con il testo "Percorso trovato" e una dimensione del font di 16 per rendere chiaro che la visualizzazione mostra il percorso trovato tra il punto di partenza e il punto di arrivo nella matrice
    plt.show() # mostro la visualizzazione grafica della matrice con il percorso trovato utilizzando la funzione show di Matplotlib, che apre una finestra con l'immagine generata


# MAIN
def main():
    prob_ostacolo = 0.3  # 30% di probabilità che una casella sia un ostacolo

    N = chiedi_dimensione_matrice() # chiedo all'utente la dimensione N della matrice
    matrice = crea_matrice(N, prob_ostacolo) # creo la matrice N x N con ostacoli generati casualmente in base alla probabilità specificata

    for riga in matrice:
        print(riga)

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

    percorso = bfs_lista(matrice, start, end) # chiamo la funzione bfs_lista per eseguire la ricerca in ampiezza (BFS) utilizzando una lista come coda, passando la matrice, il punto di partenza e il punto di arrivo come argomenti, e memorizzo il risultato nella variabile percorso

    if percorso: # se la variabile percorso contiene un percorso valido (cioè non è None), stampo il percorso trovato
        print("Percorso trovato:") # stampo un messaggio per indicare che è stato trovato un percorso
        print(percorso) # stampo il percorso trovato, che è una lista di tuple che rappresentano le coordinate dei nodi attraversati dal punto di partenza al punto di arrivo
    else: # se la variabile percorso è None, significa che non esiste un percorso valido tra il punto di partenza e il punto di arrivo, quindi stampo un messaggio per indicare che non è stato trovato alcun percorso
        print("Nessun percorso disponibile tra partenza e arrivo.") # stampo un messaggio per indicare che non è stato trovato alcun percorso valido tra il punto di partenza e il punto di arrivo, probabilmente a causa della presenza di ostacoli che bloccano tutte le possibili vie di accesso.

    visualizza_percorso(matrice, percorso, start, end) # chiamo la funzione visualizza_percorso per visualizzare graficamente la matrice con il percorso trovato, passando la matrice, il percorso, il punto di partenza e il punto di arrivo come argomenti. La funzione utilizza Matplotlib per creare una rappresentazione visiva della matrice.

if __name__ == "__main__": # good practise che rende il codice riutilizzabile come modulo
    main() # chiama la funzione main() per eseguire il programma quando viene eseguito direttamente, ma permette anche di importare le funzioni in altri moduli senza eseguire il codice principale.
    #TODO: Eliminare i commenti superflui
    #TODO: aggiungere la possibilità di scegliere tra BFS e DFS
    #TODO: aggiungere la possibilità di impostare la probabilità di ostacolo da input dell'utente
    #TODO: migliorare la visualizzazione grafica del percorso