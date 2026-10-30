# v2 — Clic: reacciona, torna a repòs i diu una frase en un globus
# Objectiu: clicar la mascota la fa canviar de cara (reacció) i, al cap d'un
# segon, torna sola a la cara neutra. A més mostra una frase aleatòria en un
# globus de diàleg que desapareix tot sol.
# Creix sobre la v1 (moviment amb rebot).

import tkinter as tk
import random

# root és la finestra PRINCIPAL de l'app (la mascota). N'hi ha una de sola.
root = tk.Tk()
# L'etiqueta mostra l'emoji; "Segoe UI Emoji" el pinta en color a Windows.
label = tk.Label(root, text="🐱", font=("Segoe UI Emoji", 64))
label.pack()

# Estat del moviment (vegeu v1):
#   x, y     -> POSICIÓ de la finestra a la pantalla.
#   direccio -> PAS: quant avança cada tic i cap on (+ dreta, - esquerra).
x = 100
y = 100
direccio = 2

ample_pantalla = root.winfo_screenwidth()

marge = ample_pantalla * 0.1
limit_esquerra = marge                      # vora esquerra: el propi marge
limit_dret = ample_pantalla - marge         # vora dreta: pantalla menys el marge

# Frases que diu la mascota quan la cliques.
frases = ["Hola!", "Qué tal?", "¡Bienvenido!"]

CARA_REPOS = "🐱"                            # cara neutra, a la qual torna
CARA_REACCIO = "😺"                          # cara en reaccionar al clic

def mou():
    global x, direccio
    x += direccio
    # Rebot: a cada paret es força el signe del pas cap a dins (evita vibrar).
    if x > limit_dret:
        direccio = -abs(direccio)           # toco la dreta -> cap a l'esquerra
    elif x < limit_esquerra:
        direccio = abs(direccio)            # toco l'esquerra -> cap a la dreta
    root.geometry(f"+{x}+{y}")
    root.after(50, mou)                      # "rellotge" de Tkinter: repeteix l'animació

def mostra_frase():
    # Crea un globus de diàleg temporal amb una frase a l'atzar.
    frase = random.choice(frases)            # tria una frase de la llista
    globus = tk.Toplevel()                   # finestra secundària (independent de root)
    globus.overrideredirect(True)            # treu barra de títol i vores -> sembla una bafarada
    tk.Label(globus, text=frase).pack()      # el text va DINS el globus (pare = globus, no root)
    globus.geometry(f"+{x}+{y - 100}")       # el col·loca sobre la mascota
    globus.after(1000, globus.destroy)       # d'aquí 1 s es tanca sol (destroy sense ())

def torna_cara():
    # Reposa la cara neutra. La crida l'after de click(), passat el temps.
    label.config(text=CARA_REPOS)

def click(event):
    label.config(text=CARA_REACCIO)          # 1) reacciona JA
    root.after(1000, torna_cara)             # 2) d'aquí 1 s, torna a repòs (torna_cara, sense ())
    mostra_frase()                           # 3) ensenya el globus amb la frase

label.bind("<Button-1>", click)

mou()               # arrenca el bucle d'animació
root.mainloop()     # cedeix el control a Tkinter (dibuixa i escolta esdeveniments)
