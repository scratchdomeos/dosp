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

 adesso vai nello sfondo e aggiungi questo script:

 ```text
[Quando la bandiera verde è stata cliccata]
                    |
    [Imposta la variabile acceso a 1]
```

Se preferisci un'immagine:


<img width="1024" height="832" alt="Immagine 2" src="https://github.com/user-attachments/assets/e6776846-b4d0-45a6-85e4-508b07c0005e" />

---

## Risolvere i problemi

Il nostro script ha un bug: la variabile `acceso` rimane 1 anche quando si spegne il sistema via start di DomeOS. Quindi aggiungete questo script:

```text
     [Quando spegni è stato ricevuto]
                    |
     [Imposta la variabile acceso a 0]
```

Poi abbiamo un'altro bug: la variabile `acceso` si vede nel visualizzatore. Andate nella sezione variabili e deselezionate `acceso`.

---

## Proporre le modifiche

Abbiamo fatto le nostre modifiche. Ora salvate il file chiamandolo `DomeOS_Issue99999 PRFILE.sb3` (in realtà come volete, basta che finisca con `PRFILE` così capisce il nostro team che è quello il file della PR).

Ora andiamo alla pagina della Repository di DOSP [`scratchdomeos/dosp`](https://github.com/scratchdomeos/dosp) e cliccate `Fork`.

Ora sul vostro fork cliccate sul "+" e "upload files".
Trascinate il file creato dove indicato (In questo caso, `DomeOS_Issue99999 PRFILE.sb3`) e cliccate su Commit Changes.

Ora, cliccate sul tasto "Compare & Pull request" e seguite tutte le istruzioni a schermo, includendo titolo e descrizione per la vostra pull request.

---

## Fine

Ora sai come fare una pull request.

