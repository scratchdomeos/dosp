# Fare un Fork

Benvenuto, Programmatore!

In questa guida scoprirai come creare un **fork** del repository di **DomeOS** e prepararlo per le tue modifiche.

---

# Cos'è un fork?

Un **fork** è una copia del repository originale presente sul tuo account GitHub.

Ti permette di lavorare liberamente senza modificare direttamente il repository ufficiale di DomeOS.

---

# Requisiti

Prima di iniziare assicurati di avere:

1. Un account GitHub.
2. Git installato.
3. Scratch installato.
4. Python 3 installato.
5. Spazio libero su disco sufficiente.

---

# Creare il fork

Apri il repository ufficiale di DOSP:

```text
https://github.com/scratchdomeos/dosp
```

In alto a destra clicca sul pulsante **Fork**.

GitHub creerà una copia del repository nel tuo account.

---

# Clonare il fork

Una volta creato il fork, clonalo sul tuo computer:

```bash
git clone https://github.com/TUO_USERNAME/dosp.git
```

Sostituisci `TUO_USERNAME` con il tuo nome utente GitHub.

---

# Compilare DomeOS

Entra nella cartella del progetto.

Su Linux e macOS:

```bash
python3 build.py
```

Su Windows:

```bash
python build.py
```

Se la build termina correttamente vedrai un output simile:

```text
Building... project.json
--snip--

Build completata! Creato: DomeOS.sb3
```

---

# Fare le modifiche

A questo punto puoi modificare `DomeOS.sb3` con Scratch seguendo la guida relativa alla funzionalità che vuoi implementare.

Quando hai finito salva il progetto.

Il nome del file può essere qualsiasi, ma **deve terminare con `FORKFILE`**, ad esempio:

```text
DomeOS_Issue99999_FORKFILE.sb3
```

---

# Caricare il file

Apri il tuo fork su GitHub.

Premi **+ → Upload files**, trascina il file `.sb3` e conferma con **Commit changes**.

Il file sarà ora disponibile nel tuo fork.

---

# Fine

Complimenti! 🎉

Hai creato il tuo fork di DomeOS e hai imparato come caricare le tue modifiche.

Ora puoi continuare con la guida **Come fare una Pull Request** per proporre le modifiche al repository ufficiale.
