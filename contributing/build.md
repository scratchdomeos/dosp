# Compilare DomeOS

Benvenuto nella guida alla compilazione di **DomeOS**!

In questa guida imparerai come compilare il progetto DomeOS partendo dal codice sorgente.

Questa procedura sarà utile ogni volta che vorrai modificare il sistema, perché DomeOS, a differenza di altri sistemi, richiede una compilazione per generare la versione utilizzabile.

---

# Requisiti

Prima di iniziare, assicurati di avere installato:

1. Un sistema operativo abbastanza recente.
2. Scratch installato.
3. Git installato.
4. Python 3 installato.
5. Spazio libero sufficiente sul disco.

Dopo aver verificato tutti i requisiti, puoi procedere con la compilazione.

---

# Clona il repository

Per prima cosa devi scaricare il codice sorgente di DomeOS.

Clona il repository di DOSP:

```bash
git clone https://github.com/scratchdomeos/dosp.git
```

Entra nella cartella del progetto:

```bash
cd dosp
```

---

# Compila DomeOS

## Linux e macOS

```bash
python3 build.py
```

## Windows

```bash
python build.py
```

Se tutto è andato a buon fine vedrai un output simile a questo:

```text
Building... project.json
--snip--

Build completata! Creato: DomeOS.sb3
```

Il file generato sarà:

```text
DomeOS.sb3
```

---

# Fine

Complimenti!

Ora sai come compilare DomeOS partendo dal codice sorgente.
