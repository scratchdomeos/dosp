import os
import zipfile


SRC_DIR = "src"

# File da ignorare dentro src
IGNORE_FILES = {
    ".DS_Store",
}

# Cartelle da ignorare dentro src
IGNORE_DIRS = {
    ".git",
    "__pycache__",
}

ZIP_NAME = "DomeOS.zip"
FINAL_NAME = "DomeOS.sb3"


def should_ignore(path):
    parts = path.split("/")

    # Controlla se una cartella è da ignorare
    for part in parts[:-1]:
        if part in IGNORE_DIRS:
            return True

    # Controlla se il file è da ignorare
    if parts[-1] in IGNORE_FILES:
        return True

    return False


# Elimina eventuali file esistenti
for file in (ZIP_NAME, FINAL_NAME):
    if os.path.exists(file):
        os.remove(file)


# Controlla che src esista
if not os.path.exists(SRC_DIR):
    print("Errore: cartella src/ non trovata")
    exit(1)


# Crea lo ZIP
with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:

    for root, dirs, files in os.walk(SRC_DIR):

        # Salta cartelle ignorate
        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIRS
        ]

        for file in files:

            full_path = os.path.join(
                root,
                file
            )

            # Percorso relativo rispetto a src/
            relative_path = os.path.relpath(
                full_path,
                SRC_DIR
            )

            # Uniforma separatori
            relative_path = relative_path.replace("\\", "/")

            if should_ignore(relative_path):
                continue

            print(f"Building... ({relative_path})")

            # IMPORTANTE:
            # Scrive il file nella root dello sb3
            zipf.write(
                full_path,
                relative_path
            )


# Rinomina .zip -> .sb3
os.rename(
    ZIP_NAME,
    FINAL_NAME
)


print(f"\nBuild completata! Creato: {FINAL_NAME}")