import time

def bfs_lista(matrice, start, end): # funzione per eseguire la ricerca in ampiezza (BFS) utilizzando una lista come coda, per trovare un percorso da start a end
    start_time = time.time()
    n = len(matrice) # ottengo la dimensione della matrice
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
            end_time = time.time()
            print(f"Tempo di esecuzione BFS: {end_time - start_time:.4f} secondi") # stampo il tempo di esecuzione della BFS con lista
            return percorso # restituisco il percorso trovato

        riga, col = nodo_corrente # scompongo il nodo corrente nelle sue coordinate (riga e colonna)
        for dr, dc in movimenti: # ciclo for per ogni possibile movimento (dr, dc) nella lista dei movimenti
            nuova_riga = riga + dr # calcolo la nuova riga dopo aver applicato il movimento dr al nodo corrente
            nuova_col = col + dc # calcolo la nuova colonna dopo aver applicato il movimento dc al nodo corrente
            nuovo_nodo = (nuova_riga, nuova_col) # creo una tupla nuovo_nodo che rappresenta le coordinate del nuovo nodo dopo aver applicato il movimento al nodo corrente
            if 0 <= nuova_riga < n and 0 <= nuova_col < n: # se le nuove coordinate sono valide (cioè all'interno dei limiti della matrice)
                if matrice[nuova_riga][nuova_col] == 0 and nuovo_nodo not in visitati: # se la casella corrispondente al nuovo nodo è libera (0) e il nuovo nodo non è già stato visitato
                    coda.append(nuovo_nodo) # aggiungo il nuovo nodo alla coda per essere visitato in futuro
                    visitati.append(nuovo_nodo) # aggiungo il nuovo nodo alla lista dei nodi visitati per evitare di visitarlo nuovamente in futuro
                    predecessore[nuovo_nodo] = nodo_corrente # aggiorno il dizionario dei predecessori per indicare che il predecessore del nuovo nodo è il nodo corrente per poter ricostruire il percorso alla fine

    return None

def dfs_lista(matrice, start, end): # funzione per eseguire la ricerca in profondità (DFS) utilizzando una lista come pila, per trovare un percorso da start a end
    start_time = time.time()
    n = len(matrice) # ottengo la dimensione della matrice
    movimenti = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)] # lista dei movimenti possibili (8 direzioni: su, giù, sinistra, destra e diagonali)
    pila = [start]  # lista che funge da pila per la DFS, inizialmente contiene solo il nodo di partenza
    visitati = [start]  # lista dei nodi già visitati, inizialmente contiene solo il nodo di partenza
    predecessore = {}  # dizionario per tenere traccia del predecessore di ogni nodo visitato per ricostruire il percorso alla fine

    while pila: # finché la pila non è vuota
        nodo_corrente = pila.pop()  # prendo l'ultimo nodo dalla pila (LIFO)
        if nodo_corrente == end:  # se il nodo corrente è il nodo di arrivo, ricostruisco il percorso usando il dizionario dei predecessori
            percorso = [] # lista per memorizzare il percorso trovato
            while nodo_corrente != start: # finché il nodo corrente non è il nodo di partenza, aggiungo il nodo corrente al percorso e aggiorno il nodo corrente al suo predecessore
                percorso.append(nodo_corrente) # aggiungo il nodo corrente al percorso
                nodo_corrente = predecessore[nodo_corrente] # aggiorno il nodo corrente al suo predecessore
            percorso.append(start) # aggiungo il nodo di partenza al percorso
            percorso.reverse() # inverto il percorso per avere l'ordine corretto da start a end
            end_time = time.time()
            print(f"Tempo di esecuzione DFS: {end_time - start_time:.4f} secondi") # stampo il tempo di esecuzione della DFS con lista
            return percorso # restituisco il percorso trovato

        riga, col = nodo_corrente # scompongo il nodo corrente nelle sue coordinate (riga e colonna)
        for dr, dc in movimenti: # ciclo for per ogni possibile movimento (dr, dc) nella lista dei movimenti
            nuova_riga = riga + dr # calcolo la nuova riga dopo aver applicato il movimento dr al nodo corrente
            nuova_col = col + dc # calcolo la nuova colonna dopo aver applicato il movimento dc al nodo corrente
            nuovo_nodo = (nuova_riga, nuova_col) # creo una tupla nuovo_nodo che rappresenta le coordinate del nuovo nodo dopo aver applicato il movimento al nodo corrente
            if 0 <= nuova_riga < n and 0 <= nuova_col < n: # se le nuove coordinate sono valide (cioè all'interno dei limiti della matrice)
                if matrice[nuova_riga][nuova_col] == 0 and nuovo_nodo not in visitati: # se la casella corrispondente al nuovo nodo è libera (0) e il nuovo nodo non è già stato visitato
                    pila.append(nuovo_nodo) # aggiungo il nuovo nodo alla pila per essere visitato in futuro
                    visitati.append(nuovo_nodo) # aggiungo il nuovo nodo alla lista dei nodi visitati per evitare di visitarlo nuovamente in futuro
                    predecessore[nuovo_nodo] = nodo_corrente # aggiorno il dizionario dei predecessori per indicare che il predecessore del nuovo nodo è il nodo corrente per poter ricostruire il percorso alla fine
