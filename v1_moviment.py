# v1 — Moviment amb rebot
# Objectiu: la mascota avança sola i, en arribar a un marge de la pantalla,
# rebota cap a l'altre costat sense sortir-ne mai.
# Creix sobre la v0 (finestra base) afegint l'animació.

import tkinter as tk

root = tk.Tk()
# L'etiqueta mostra l'emoji; "Segoe UI Emoji" el pinta en color a Windows.
label = tk.Label(root, text="🐱", font=("Segoe UI Emoji", 64))
label.pack()

# Estat del moviment:
#   x, y     -> POSICIÓ de la finestra a la pantalla (on és la mascota).
#   direccio -> PAS: quant avança cada tic i cap on. Positiu = dreta, negatiu = esquerra.
# Són dues coses diferents: x és "on sóc", direccio és "cap on faig el pas".
x = 100
y = 100
direccio = 2

# Amplada real de la pantalla en píxels (depèn del monitor).
ample_pantalla = root.winfo_screenwidth()

# Deixem un marge del 10% a banda i banda perquè no toqui les vores exactes.
marge = ample_pantalla * 0.1
limit_esquerra = marge                      # vora esquerra: el propi marge
limit_dret = ample_pantalla - marge         # vora dreta: tota la pantalla menys el marge

def mou():
    # global perquè modifiquem x i direccio, que viuen fora de la funció.
    global x, direccio

    # 1) Avança: nova posició = posició actual + pas.
    x += direccio

    # 2) Rebot. Cada branca és una parella "quina paret toco -> cap on he d'anar":
    #    abs(direccio) dona el pas sempre positiu (dreta); -abs(...) sempre negatiu (esquerra).
    #    Forçar el signe (en lloc de girar-lo amb -direccio) evita que vibri contra la paret.
    if x > limit_dret:
        direccio = -abs(direccio)           # toco la dreta -> força cap a l'esquerra
    elif x < limit_esquerra:
        direccio = abs(direccio)            # toco l'esquerra -> força cap a la dreta

    # 3) Reposiciona la finestra a la nova x (la y no canvia, es mou en horitzontal).
    root.geometry(f"+{x}+{y}")

    # 4) Es torna a programar d'aquí 50 ms: és el "rellotge" de Tkinter que fa l'animació.
    #    mou (sense parèntesis) = li donem la funció perquè la cridi ell després.
    root.after(50, mou)

def click(event):
    # Esbós de reacció al clic (pertany pròpiament a la v2): canvia de cara.
    label.config(text="😺")

label.bind("<Button-1>", click)

mou()               # arrenca el bucle d'animació
root.mainloop()     # cedeix el control a Tkinter (dibuixa i escolta esdeveniments)