"""
Plant Disease Detection - Model Download Helper Script
-------------------------------------------------------
This script downloads the official, pretrained MobileNetV2 ONNX model
and its class configuration (trained on the PlantVillage benchmark dataset)
from Hugging Face.

Run this script once if you are setting up the project on a new machine:
    python download_model.py
"""

import os
import urllib.request
import sys

# Directory where the model and config will be saved
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model")
CONFIG_PATH = os.path.join(MODEL_DIR, "config.json")
MODEL_PATH = os.path.join(MODEL_DIR, "model.onnx")

# Hugging Face URLs for the official MobileNetV2 Plant Disease model
CONFIG_URL = "https://huggingface.co/onnx-community/mobilenet_v2_1.0_224-plant-disease-identification-ONNX/raw/main/config.json"
MODEL_URL = "https://huggingface.co/onnx-community/mobilenet_v2_1.0_224-plant-disease-identification-ONNX/resolve/main/onnx/model.onnx"


def download_file(url: str, destination: str, description: str) -> None:
    """
    Downloads a remote file with progress reporting and user-agent headers.
    """
    print(f"[*] Downloading {description}...")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PlantDiseaseApp/1.0"}
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response, open(destination, "wb") as out_file:
        total_size = int(response.headers.get("Content-Length", 0))
        downloaded = 0
        chunk_size = 64 * 1024  # 64 KB chunks

        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            out_file.write(chunk)
            downloaded += len(chunk)
            if total_size > 0:
                percent = (downloaded / total_size) * 100
                mb_done = downloaded / (1024 * 1024)
                mb_total = total_size / (1024 * 1024)
                print(f"\r    Progress: {percent:5.1f}% ({mb_done:.1f}/{mb_total:.1f} MB)", end="", flush=True)
        print("\n[+] Download completed successfully.")


def setup_model() -> bool:
    """
    Ensures model directory exists and downloads missing model files.
    """
    os.makedirs(MODEL_DIR, exist_ok=True)

    # 1. Check or download config.json (contains 38 class names)
    if not os.path.exists(CONFIG_PATH) or os.path.getsize(CONFIG_PATH) == 0:
        try:
            download_file(CONFIG_URL, CONFIG_PATH, "model config (config.json)")
        except Exception as e:
            print(f"[-] Failed to download config.json: {e}", file=sys.stderr)
            return False
    else:
        print(f"[i] Config file already present ({os.path.getsize(CONFIG_PATH)} bytes).")

    # 2. Check or download model.onnx (9.2 MB MobileNetV2 ONNX weights)
    if not os.path.exists(MODEL_PATH) or os.path.getsize(MODEL_PATH) < 1000:
        try:
            download_file(MODEL_URL, MODEL_PATH, "pretrained ONNX model (model.onnx ~9.2 MB)")
        except Exception as e:
            print(f"[-] Failed to download model.onnx: {e}", file=sys.stderr)
            return False
    else:
        print(f"[i] Model weights already present ({os.path.getsize(MODEL_PATH)} bytes).")

    print("[+] Model setup is complete and ready for inference!")
    return True


if __name__ == "__main__":
    success = setup_model()
    if not success:
        sys.exit(1)
