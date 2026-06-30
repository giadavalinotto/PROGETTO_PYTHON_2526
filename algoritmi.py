import time

def costruisci_percorso(predecessore, start, nodo_corrente):
    percorso = []  # lista per memorizzare il percorso trovato
    while nodo_corrente != start: # finché il nodo corrente non è il nodo di partenza
        percorso.append(nodo_corrente) # aggiungo il nodo corrente alla lista del percorso
        nodo_corrente = predecessore[nodo_corrente] # aggiorno al nodo precedente del nodo corrente
    percorso.append(start) # aggiungo il nodo di partenza alla lista del percorso
    percorso.reverse() # inverto la lista per ottenere il percorso corretto dalla partenza all'arrivo
    return percorso

def bfs_lista(matrice, start, end):
    start_time = time.time()
    n = len(matrice)
    movimenti = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)] # (8 direzioni: su, giù, sinistra, destra e diagonali)
    coda = [start]  # lista che contiene i nodi da visitare
    visitati = [start]  # lista dei nodi già visitati
    predecessore = {}  # dizionario per tenere traccia del predecessore di ogni nodo visitato e ricostruire il percorso alla fine

    while coda: # finché la coda non è vuota
        nodo_corrente = coda.pop(0)  # prendo il primo nodo dalla coda (FIFO)
        
        if nodo_corrente == end:  # se il nodo corrente è il nodo di arrivo
            percorso = costruisci_percorso(predecessore, start, nodo_corrente) # lista per memorizzare il percorso trovato
            end_time = time.time()
            print(f"Tempo di esecuzione BFS: {end_time - start_time:.4f} secondi")
            return percorso

        riga, col = nodo_corrente # scompongo il nodo corrente nelle sue coordinate (riga e colonna)
        for dr, dc in movimenti: # ciclo for per ogni possibile movimento (dr, dc) nella lista dei movimenti
            nuova_riga = riga + dr # calcolo la nuova riga dopo aver applicato il movimento dr al nodo corrente
            nuova_col = col + dc # calcolo la nuova colonna dopo aver applicato il movimento dc al nodo corrente
            nuovo_nodo = (nuova_riga, nuova_col) # creo una tupla nuovo_nodo che rappresenta le coordinate del nuovo nodo
            if 0 <= nuova_riga < n and 0 <= nuova_col < n: # se le nuove coordinate sono all'interno dei limiti della matrice
                if matrice[nuova_riga][nuova_col] == 0 and nuovo_nodo not in visitati: # se la casella corrispondente al nuovo nodo è libera (0) e il nuovo nodo non è già stato visitato
                    coda.append(nuovo_nodo) # aggiungo il nuovo nodo alla coda per essere visitato in futuro
                    visitati.append(nuovo_nodo) # aggiungo il nuovo nodo alla lista dei nodi visitati per evitare di visitarlo nuovamente in futuro
                    predecessore[nuovo_nodo] = nodo_corrente # aggiorno per indicare che il predecessore del nuovo nodo è il nodo corrente

    return None # se la coda si svuota senza trovare il nodo di arrivo, restituisco None per indicare che non è stato trovato alcun percorso

def dfs_lista(matrice, start, end):
    start_time = time.time()
    n = len(matrice)
    movimenti = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    pila = [start]  # lista che funziona come pila dei nodi da visitare (LIFO)
    visitati = [start]  # lista dei nodi già visitati
    predecessore = {}

    while pila: # finché la pila non è vuota
        nodo_corrente = pila.pop()  # prendo l'ultimo nodo dalla pila (LIFO)
        
        if nodo_corrente == end:
            percorso = costruisci_percorso(predecessore, start, nodo_corrente)
            end_time = time.time()
            print(f"Tempo di esecuzione DFS: {end_time - start_time:.4f} secondi")
            return percorso

        riga, col = nodo_corrente
        for dr, dc in movimenti:
            nuova_riga = riga + dr
            nuova_col = col + dc
            nuovo_nodo = (nuova_riga, nuova_col)
            if 0 <= nuova_riga < n and 0 <= nuova_col < n:
                if matrice[nuova_riga][nuova_col] == 0 and nuovo_nodo not in visitati:
                    pila.append(nuovo_nodo)
                    visitati.append(nuovo_nodo)
                    predecessore[nuovo_nodo] = nodo_corrente