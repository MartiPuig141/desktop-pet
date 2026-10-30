# v0 — Finestra base de la mascota d'escriptori
# Objectiu: una finestra de Tkinter amb l'emoji de la mascota en una posició fixa.
# Encara no es mou ni reacciona; és la base sobre la qual creixen les versions següents.

import tkinter as tk

# root és la finestra principal. Tota app de Tkinter en té una.
root = tk.Tk()

# L'etiqueta (Label) és el widget que mostra l'emoji.
# La font "Segoe UI Emoji" el pinta en color a Windows; .pack() el col·loca dins la finestra.
label = tk.Label(root, text="🐱", font=("Segoe UI Emoji", 64))
label.pack()

# Posició inicial de la finestra a la pantalla (cantonada superior esquerra).
# El format de geometry és "+x+y": píxels des de l'origen (dalt a l'esquerra).
x = 100
y = 100
root.geometry(f"+{x}+{y}")

# mainloop cedeix el control a Tkinter: dibuixa la finestra i es queda
# escoltant esdeveniments fins que la tanques. Sense això, el programa acabaria de cop.
root.mainloop()
