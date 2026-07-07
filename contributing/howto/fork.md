# Fare un Fork

Benvenuto, Programmatore!

In questa guida scoprirai come contribuire a **DomeOS** creando una Pull Request.

---

# Requisiti

Prima di iniziare, assicurati di avere:

1. Un sistema operativo abbastanza recente.
2. Scratch installato.
3. Git installato.
4. Python 3 installato.
5. Spazio libero su disco sufficiente.

Con questi requisiti sei pronto per contribuire al progetto.

---

# Pensare alla funzionalità

Prima di modificare il progetto, è importante sapere cosa vuoi aggiungere o correggere.

In questa guida useremo come esempio la seguente issue:

> **Issue #99999**  
> Vorrei introdurre una variabile `acceso` che vale `1` quando DomeOS è acceso.

---

# Compilare DomeOS

Per prima cosa clona il repository di DOSP:

```bash
git clone https://github.com/scratchdomeos/dosp.git
```

Entra nella cartella del progetto ed esegui la build.

Su Linux e macOS:

```bash
python3 build.py
```

Su Windows:

```bash
python build.py
```

Se tutto è andato a buon fine vedrai un output simile a questo:

```text
Building... project.json
--snip--

Build completata! Creato: DomeOS.sb3
```

---

# Fare la modifica

Apri `DomeOS.sb3` con Scratch.

Vai nella categoria **Variables** e crea una nuova variabile chiamata `acceso`.

<img width="2772" height="2672" alt="Immagine 1" src="https://github.com/user-attachments/assets/fbfff968-0bac-481f-8b5e-ffe6755d574c" />

Successivamente apri lo **Stage** e aggiungi questo script:

```text
[when green flag clicked]
          │
[set acceso to 1]
```

Se preferisci, puoi seguire questa immagine:

<img width="1024" height="832" alt="Immagine 2" src="https://github.com/user-attachments/assets/e6776846-b4d0-45a6-85e4-508b07c0005e" />

---

# Risolvere i problemi

Il nostro script presenta un piccolo bug: la variabile `acceso` rimane uguale a `1` anche quando il sistema viene spento dal menu Start.

Per risolvere il problema aggiungi questo script:

```text
[when I receive spento]
          │
[set acceso to 0]
```

Infine, nascondi la variabile `acceso` deselezionandola nella categoria **Variables**, così non verrà mostrata durante l'utilizzo di DomeOS.

---

# Mettilo nel fork

Ora salva il progetto.

Puoi chiamarlo come preferisci, ma il nome **deve terminare con `FORKFILE`**, ad esempio:

```text
DomeOS_Issue99999_FORKFILE.sb3
```

Questo permette al team di riconoscere facilmente il file della Pull Request.

Successivamente visita il repository:

https://github.com/scratchdomeos/dosp

e clicca su **Fork**.

Nel tuo fork premi **+ → Upload files**, trascina il file appena creato e conferma con **Commit changes**.

---

# Fine

Complimenti! 🎉

Hai imparato come creare un Fork per DomeOS.

Grazie per il tuo contributo al progetto!
