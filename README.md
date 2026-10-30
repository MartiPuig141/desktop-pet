# desktop-pet 🐱

Una mascota d'escriptori interactiva feta amb **Tkinter** (la llibreria gràfica que ve de sèrie amb Python). Un gatet que camina per la pantalla, reacciona als clics, es pot arrossegar, respon a missatges i té un menú de clic dret.

És un **projecte d'aprenentatge**: l'objectiu era posar a prova i reforçar conceptes de Python (funcions, control de flux, esdeveniments) construint alguna cosa visual i divertida. El codi està partit en versions incrementals perquè es vegi com creix pas a pas.

## Com executar-ho

Cal Python 3 amb Tkinter (inclòs a la instal·lació estàndard de Python a Windows i macOS; a Linux pot caldre `sudo apt install python3-tk`). No cal instal·lar cap paquet extra.

```bash
python3 v5_menu.py
```

Cada versió és independent i es pot executar sola per veure l'evolució.

## Versions

El projecte s'ha construït afegint **una capacitat per versió**, cada una al seu fitxer:

| Fitxer | Què afegeix |
|---|---|
| `v0_finestra.py` | Finestra base amb l'emoji en una posició fixa |
| `v1_moviment.py` | La mascota camina sola i rebota contra els marges de la pantalla |
| `v2_clic.py` | Clic: canvia de cara i diu una frase en un globus |
| `v3_arrossegar.py` | Es pot agafar i moure amb el ratolí |
| `v4_xat.py` | Clic dret obre un quadre de text; respon segons paraules clau |
| `v5_menu.py` | Menú de clic dret + finestra sense vores i sempre a sobre (versió final) |

## Controls (v5)

- **Clic esquerre** — la mascota reacciona (canvia de cara i diu una frase).
- **Arrossegar** — agafa-la i mou-la on vulguis.
- **Clic dret** — obre el menú: "Parla amb mi" (xat) o "Tancar".

## Tecnologia

Només Python + Tkinter. Sense dependències externes.

## Estat

Projecte d'aprenentatge **funcional** (v0–v5 completes i executables). En millora activa.

### Pendent / roadmap

- Distingir el clic net de l'arrossegament (ara el clic esquerre fa les dues coses alhora).
- Que el globus de diàleg segueixi la mascota mentre camina, en lloc de quedar-se quiet.
- Treure les frases i les expressions a un fitxer de configuració, en lloc de tenir-les al codi.
- Sprites dibuixats (Pillow) en lloc d'emojis; guardar l'estat entre execucions (JSON).
