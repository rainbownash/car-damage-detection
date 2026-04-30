import gdown
import zipfile
import os

DATA_URL = "https://drive.google.com/drive/folders/1a6xth8YNQcUfeP79VVCEVxuOpZdJ7nKL?usp=sharing"

ZIP_NAME = "dataset.zip"
OUTPUT_DIR = "dataset"

def download_dataset():
    print("📦 Descargando dataset...")

    gdown.download(DATA_URL, ZIP_NAME, quiet=False)

    print("📂 Descomprimiendo dataset...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with zipfile.ZipFile(ZIP_NAME, 'r') as zip_ref:
        zip_ref.extractall(OUTPUT_DIR)

    print(f"✅ Dataset listo en: {OUTPUT_DIR}")

if __name__ == "__main__":
    download_dataset()
