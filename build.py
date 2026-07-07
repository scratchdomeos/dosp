import os
import zipfile

# File da ignorare
IGNORE_FILES = {
    "build.py",
    "README.md",
    "LICENSE",
    "DomeOS.zip",
    "DomeOS.sb3"
}

# Cartelle da ignorare
IGNORE_DIRS = {
    ".git",
    "contributing",
}

ZIP_NAME = "DomeOS.zip"
FINAL_NAME = "DomeOS.sb3"


def should_ignore(path):
    parts = path.split(os.sep)

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

# Crea lo ZIP
with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk("."):
        # Salta le cartelle ignorate
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, ".")

            if should_ignore(relative_path):
                continue

            print(f"Building... ({relative_path})")
            zipf.write(full_path, relative_path)

# Rinomina .zip -> .sb3
os.rename(ZIP_NAME, FINAL_NAME)

print(f"\nBuild completata! Creato: {FINAL_NAME}")
