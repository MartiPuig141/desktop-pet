# desktop-pet 🐱

An interactive desktop pet built with **Tkinter** (Python's built-in GUI library). A little cat that walks around your screen, reacts to clicks, can be dragged, replies to messages and has a right-click menu.

This is a **learning project**: the goal was to practise and reinforce core Python concepts (functions, control flow, events) by building something visual and fun. The code is split into incremental versions so you can follow how it grows step by step.

## How to run

Requires Python 3 with Tkinter (included in the standard Python install on Windows and macOS; on Linux you may need `sudo apt install python3-tk`). No extra packages needed.

```bash
python3 v5_menu.py
```

Each version is standalone and can be run on its own to see the progression.

## Versions

The project was built by adding **one capability per version**, each in its own file:

| File | What it adds |
|---|---|
| `v0_finestra.py` | Base window with the emoji at a fixed position |
| `v1_moviment.py` | The pet walks on its own and bounces off the screen edges |
| `v2_clic.py` | Click: changes face and says a phrase in a speech bubble |
| `v3_arrossegar.py` | Can be grabbed and moved with the mouse |
| `v4_xat.py` | Right-click opens a text box; replies based on keywords |
| `v5_menu.py` | Right-click menu + borderless, always-on-top window (final version) |

(Filenames are in Catalan, the author's working language; comments inside the code are Catalan too.)

## Controls (v5)

- **Left click** — the pet reacts (changes face and says a phrase).
- **Drag** — grab it and move it anywhere.
- **Right click** — opens the menu: "Parla amb mi" (chat) or "Tancar" (quit).

## Tech

Python + Tkinter only. No external dependencies.

## Status

A **working** learning project (v0–v5 complete and runnable). Actively being improved.

### Roadmap

- Tell a plain click apart from a drag (right now a left click does both at once).
- Make the speech bubble follow the pet while it walks, instead of staying put.
- Move the phrases and expressions into a config file instead of hardcoding them.
- Real drawn sprites (Pillow) instead of emojis; persist state between runs (JSON).
