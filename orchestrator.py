import subprocess
import sys
import os
from time import time
import config

def run_pipeline(input_image_name):
    for folder in config.REQUIRED_FOLDERS:
        os.makedirs(folder, exist_ok=True)

    timestamp = int(time())
    
    input_image_path = os.path.join(config.INPUT_DIR, input_image_name)
    color_json_path = os.path.join(config.JSON_DIR, f"{timestamp}.json")
    output_image_path = os.path.join(config.OUTPUT_DIR, f"{timestamp}.png")
    
    print(f"[*] Starting pipeline for: {input_image_name}")

    subprocess.run(
        ["uv", "run", "--quiet", "analyzer.py", input_image_path, color_json_path],
        capture_output=True,
        text=True,
        check=True
    )
    print("[+] Step 1: Colors extracted.")

    subprocess.run(
        ["uv", "run", "--quiet", "visualizer.py", color_json_path, output_image_path],
        check=True
    )
    
    full_path = os.path.abspath(output_image_path)
    print(f"[+] Etap 2: Image generated.")
    print(f"\n[SUCCESS] Path to file: {full_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide the path to the input image!")
    else:
        run_pipeline(sys.argv[1])