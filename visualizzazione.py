import matplotlib.pyplot as plt # importo la libreria matplotlib.pyplot per visualizzare graficamente la matrice con il percorso trovato
import numpy as np # importo la libreria numpy per manipolare array e matrici, utilizzando l'alias np per semplificare la sintassi

def stampa_percorso(percorso, algoritmo): # funzione per stampare il percorso trovato in modo chiaro, indicando l'algoritmo utilizzato (BFS o DFS)
    if percorso: # se la variabile percorso contiene un percorso valido (cioè non è None), stampo il percorso trovato
        print(f"Percorso trovato con {algoritmo}:") # stampo un messaggio per indicare che è stato trovato un percorso, specificando l'algoritmo utilizzato (BFS o DFS)
        print(percorso) # stampo il percorso trovato, che è una lista di tuple che rappresentano le coordinate dei nodi attraversati dal punto di partenza al punto di arrivo
    else: # se la variabile percorso è None, significa che non esiste un percorso valido tra il punto di partenza e il punto di arrivo, quindi stampo un messaggio per indicare che non è stato trovato alcun percorso
        print(f"Nessun percorso disponibile tra partenza e arrivo con {algoritmo}.") # stampo un messaggio per indicare che non è stato trovato alcun percorso valido tra il punto di partenza e il punto di arrivo utilizzando l'algoritmo specificato (BFS o DFS), probabilmente a causa della presenza di ostacoli che bloccano tutte le possibili vie di accesso.

def visualizza_percorso(matrice, percorso, start, end, algoritmo): # funzione per visualizzare graficamente la matrice con il percorso trovato, evidenziando start, end e il percorso stesso

    n = len(matrice) # ottengo la dimensione della matrice
    array = np.array(matrice) # converto la matrice in un array numpy per facilitare la manipolazione e la visualizzazione grafica

    # Creo un array RGB per i colori
    colori = np.zeros((n, n, 3)) # inizializzo un array di zeri con dimensioni (N, N, 3) per rappresentare i colori RGB di ogni cella della matrice, dove N è la dimensione della matrice e 3 rappresenta i canali di colore (rosso, verde, blu)
    for r in range(n): # ciclo for per ogni riga della matrice
        for c in range(n): # ciclo for per ogni colonna della matrice
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
    plt.xticks(range(n)) # imposto i tick dell'asse x per mostrare le coordinate delle colonne da 0 a N-1
    plt.yticks(range(n)) # imposto i tick dell'asse y per mostrare le coordinate delle righe da 0 a N-1
    plt.grid(color='gray', linestyle='-', linewidth=1) # aggiungo una griglia grigia con linee continue e spessore di 1 per migliorare la visibilità delle celle nella matrice
    plt.title("Percorso trovato con " + algoritmo, fontsize=16) # aggiungo un titolo alla visualizzazione con il testo "Percorso trovato" e una dimensione del font di 16 per rendere chiaro che la visualizzazione mostra il percorso trovato tra il punto di partenza e il punto di arrivo nella matrice
    plt.show() # mostro la visualizzazione grafica della matrice con il percorso trovato utilizzando la funzione show di Matplotlib, che apre una finestra con l'immagine generata

