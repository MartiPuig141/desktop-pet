# v4 — Xat: quadre de text i resposta per paraules clau
# Objectiu: clic dret sobre la mascota obre un quadre on escrius; en prémer
# Enter, la mascota respon segons paraules clau (hola, adeu...) en un globus.
# Creix sobre la v3 (moviment + clic + arrossegar).

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
arrossegant = False                         # True mentre s'arrossega amb el ratolí

ample_pantalla = root.winfo_screenwidth()   # amplada real de la pantalla (adaptatiu)

marge = ample_pantalla * 0.1
limit_esquerra = marge                      # vora esquerra: el propi marge
limit_dret = ample_pantalla - marge         # vora dreta: pantalla menys el marge

# Frases que diu la mascota quan la cliques.
frases = ["Hola!", "Qué tal?", "¡Bienvenido!"]

CARA_REPOS = "🐱"                            # cara neutra, a la qual torna
CARA_REACCIO = "😺"                          # cara en reaccionar al clic

def mou():
    global x, direccio
    # Només camina si NO s'està arrossegant (si no, dit i animació es barallen).
    if not arrossegant:
        x += direccio
        # Rebot: a cada paret es força el signe del pas cap a dins (evita vibrar).
        if x > limit_dret:
            direccio = -abs(direccio)       # toco la dreta -> cap a l'esquerra
        elif x < limit_esquerra:
            direccio = abs(direccio)        # toco l'esquerra -> cap a la dreta
        root.geometry(f"+{x}+{y}")
    # L'after queda FORA de l'if: el rellotge batega sempre, fins i tot
    # mentre s'arrossega, perquè en deixar anar la caminada pugui reprendre.
    root.after(50, mou)

def mostra_frase():
    # Mostra un globus amb una frase aleatòria, que desapareix sola.
    diu(random.choice(frases))
    
def torna_cara():
    # Reposa la cara neutra. La crida l'after de click(), passat el temps.
    label.config(text=CARA_REPOS)

def click(event):
    # <Button-1> fa dues feines: la reacció de la v2 i preparar l'arrossegament.
    global desplacament_x, desplacament_y, arrossegant
    # Desplaçament = per quin punt de la mascota l'he agafat (cursor dins el widget).
    desplacament_x = event.x
    desplacament_y = event.y
    arrossegant = True                       # comença l'arrossegament
    label.config(text=CARA_REACCIO)          # 1) reacciona JA
    root.after(1000, torna_cara)             # 2) d'aquí 1 s, torna a repòs
    mostra_frase()                           # 3) ensenya el globus amb la frase

def moure(event):
    # <B1-Motion>: salta moltes vegades mentre mous amb el botó premut.
    global x, y
    # La finestra va on és el cursor en pantalla (x_root), menys el desplaçament,
    # perquè el punt que has agafat segueixi enganxat sota el cursor.
    x = event.x_root - desplacament_x
    y = event.y_root - desplacament_y
    root.geometry(f"+{x}+{y}")

def deixar(event):
    # <ButtonRelease-1>: deixes anar -> la caminada automàtica es reprèn.
    global arrossegant
    arrossegant = False
    
def diu(text):
    # Mostra 'text' en un globus temporal. Reutilitzable: val tant per a les
    # frases aleatòries del clic com per a les respostes del xat (evita duplicar).
    globus = tk.Toplevel()
    globus.overrideredirect(True)            # sense vores -> sembla una bafarada
    tk.Label(globus, text=text).pack()
    globus.geometry(f"+{x}+{y - 100}")       # sobre la mascota
    globus.after(2000, globus.destroy)       # es tanca sol als 2 s

def obre_xat(event):
    # FUNCIÓ 1 del xat: obre el quadre d'entrada i ARMA la funció 2.
    global entry                             # global perquè processa() hi accedeixi
    finestra = tk.Toplevel()                 # finestreta del xat
    entry = tk.Entry(finestra)               # camp on l'usuari escriu
    entry.pack()
    entry.focus()                            # el cursor hi va directe, sense clicar
    entry.bind("<Return>", processa)         # en prémer Enter -> processa (funció 2)

def processa(event):
    # FUNCIÓ 2 del xat: llegeix el text i respon segons paraules clau.
    # .lower() passa tot a minúscules perquè "Hola", "HOLA" i "hola" encaixin igual.
    text = entry.get().lower()
    # 'in' comprova si la paraula és DINS el text. El primer if/elif que encaixi
    # guanya i la resta se salta (per això l'ordre de les branques importa).
    if "hola" in text:
        diu("Hola! 😺")
    elif "adéu" in text or "adeu" in text:
        diu("Adéu! 😿")
    else:
        diu("No sé que respondre 😼")

label.bind("<Button-1>", click)              # prémer: reacciona i prepara l'arrossegament
label.bind("<B1-Motion>", moure)             # moure amb botó premut: arrossega
label.bind("<ButtonRelease-1>", deixar)      # deixar anar: torna a caminar
label.bind("<Button-3>", obre_xat)              # botó dret: obre la finestra d'entrada de text

mou()               # arrenca el bucle d'animació
root.mainloop()     # cedeix el control a Tkinter (dibuixa i escolta esdeveniments)
