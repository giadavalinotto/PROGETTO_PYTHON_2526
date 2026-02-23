# 🗺️ Pathfinder — Ricerca su Matrice con BFS e DFS

> Trova il percorso tra due punti su una griglia generata casualmente, scegliendo tra due algoritmi di ricerca classici: **BFS** e **DFS**. Il risultato viene visualizzato graficamente.

---

## ✨ Funzionalità

- 🎲 Generazione casuale della matrice con probabilità di ostacolo configurabile
- 🔀 Scelta dell'algoritmo di ricerca: **BFS** o **DFS**
- 🧭 Movimenti in **8 direzioni** (incluse le diagonali)
- 🎨 Visualizzazione grafica del percorso con colori distinti
- ✅ Gestione degli errori sull'input utente

---

## 🚀 Requisiti e installazione

- Python 3.x
- matplotlib
- numpy

```bash
pip install matplotlib numpy
```

---

## ▶️ Utilizzo

```bash
python main.py
```

Il programma guiderà l'utente passo per passo:

1. Dimensione `N` della matrice
2. Probabilità che una cella sia un ostacolo (es. `0.3` per il 30%)
3. Algoritmo di ricerca: `1` per BFS, `2` per DFS
4. Coordinate del punto di **partenza**
5. Coordinate del punto di **arrivo**

---

## 🖼️ Legenda colori

| Colore | Significato |
|--------|-------------|
|  Nero | Ostacolo |
|  Bianco | Cella libera |
|  Viola | Partenza / Arrivo |
|  Lilla | Percorso trovato |

---

## 🧠 BFS vs DFS

| | BFS | DFS |
|---|---|---|
| **Strategia** | Esplora per livelli concentrici | Esplora in profondità lungo un ramo |
| **Percorso** | ✅ Garantisce il più breve | ❌ Non garantisce il più breve |
| **Memoria** | Più memoria richiesta | Meno memoria richiesta |

---

## 📁 Struttura del progetto

```
├── main.py      # file principale
└── README.md
```

---

## 👤 Autore

Progetto realizzato per il corso di **Programmazione Avanzata: Python e Arduino**.