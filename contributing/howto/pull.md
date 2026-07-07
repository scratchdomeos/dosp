# Fare una pull request

Benvenuto Programmatore!
Qui scoprirai come fare una pull request!

---

## Requisiti

1. Un sistema operativo abbastanza recente
2. Scratch installato
3. Git installato
4. Python 3 Installato
5. Spazio su disco sufficiente

Questi requisiti permettono di poter fare una pull request.

---

## Pensare alla funzionalità

Dobbiamo pensare alla funzionalità che vogliamo aggiungere. In questo esempio, ci immagineremo l'issue #99999.

>**Issue #99999:** \
>Vorrei introdurre una variabile `acceso` che è 1 se si sta usando DomeOS.

---

## Compilare DomeOS

Ora che abbiamo chiara la funzionalità, dobbiamo clonare il repository del DOSP. Nel terminale digitiamo:

```bash
git clone https://github.com/scratchdomeos/dosp.git
```

Ora compileremo DomeOS. Nel terminale digitamo:

```bash
python3 build.py
```

o su Windows:

```bash
python build.py
```

Dovrebbe apparire qualcosa del genere:

```text
Building... project.json
--snip--

Build completata! Creato: DomeOS.sb3
```

---

## Fare la modifica

Ora apri il file `DomeOS.sb3` in Scratch.

Nell'editor, clicca nella sezione "Variabili" e crea una nuova variabile chiamata `acceso`:

<img width="2772" height="2672" alt="Immagine 1" src="https://github.com/user-attachments/assets/fbfff968-0bac-481f-8b5e-ffe6755d574c" />
