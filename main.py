from matplotlib import pyplot as plt
from matrice import crea_matrice
from input_utils import chiedi_dimensione_matrice, leggi_coordinata
from algoritmi import bfs_lista, dfs_lista
from visualizzazione import stampa_percorso, visualizza_percorso

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

    n = chiedi_dimensione_matrice()
    matrice = crea_matrice(n, prob_ostacolo)

    for riga in matrice:
        print(riga)

    # Coordinate del punto di partenza
    start_row = leggi_coordinata(n, "Inserisci la riga del punto di partenza: ")
    start_col = leggi_coordinata(n, "Inserisci la colonna del punto di partenza: ")
    start = (start_row, start_col) # creo una tupla che contiene le coordinate del punto di partenza (riga, colonna)

    # Coordinate del punto di arrivo
    while True:
        end_row = leggi_coordinata(n, "Inserisci la riga del punto di arrivo: ")
        end_col = leggi_coordinata(n, "Inserisci la colonna del punto di arrivo: ")
        end = (end_row, end_col) # creo una tupla che contiene le coordinate del punto di arrivo (riga, colonna)
        if end != start:
            break
        else:
            print("Il punto di arrivo non può coincidere con il punto di partenza.")

    # Imposto i valori come liberi (0)nella matrice
    matrice[start[0]][start[1]] = 0
    matrice[end[0]][end[1]] = 0

    # Stampa
    for riga in matrice:
        print(riga)

    percorso = bfs_lista(matrice, start, end) # la ricerca in ampiezza usa una logiga FIFO e usa una lista come coda
    stampa_percorso(percorso, "BFS")
    visualizza_percorso(matrice, percorso, start, end, "BFS")

    percorso = dfs_lista(matrice, start, end) # la ricerca in profondità usa una logica LIFO e usa una lista come pila
    stampa_percorso(percorso, "DFS")
    visualizza_percorso(matrice, percorso, start, end, "DFS")

    plt.show() # mostra la finestra con la visualizzazione dei percorsi


if __name__ == "__main__": # good practise che rende il codice riutilizzabile come modulo
    main() # chiama la funzione main() per eseguire il programma quando viene eseguito direttamente