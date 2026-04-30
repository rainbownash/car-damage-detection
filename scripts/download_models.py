import gdown
import zipfile
import os

MODEL_URL = "https://drive.google.com/drive/folders/1QMl2XjKZnMQRKCmH0DSFOZ7UGcAE3SZR?usp=share_link"

ZIP_NAME = "models.zip"
OUTPUT_DIR = "models"

def download_models():
    print("🧠 Descargando modelos...")

    gdown.download(MODEL_URL, ZIP_NAME, quiet=False)

    print("📂 Descomprimiendo modelos...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with zipfile.ZipFile(ZIP_NAME, 'r') as zip_ref:
        zip_ref.extractall(OUTPUT_DIR)

    print(f"✅ Modelos listos en: {OUTPUT_DIR}")

if __name__ == "__main__":
    download_models()
