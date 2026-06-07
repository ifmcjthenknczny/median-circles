import subprocess
import sys
import os
from time import time
import config

def run_pipeline(input_image_filename):
    for folder in config.DIRECTORIES.values():
        os.makedirs(folder, exist_ok=True)

    input_image_path = os.path.join(config.DIRECTORIES["INPUT"], input_image_filename)

    if not os.path.exists(input_image_path):
        print(f'[-] Input file does not exist. Check file extension and whether it exists in the "input" directory')
        return

    image_name = input_image_filename.rsplit('.', 1)[0]

    color_json_path = os.path.join(config.DIRECTORIES["JSON"], f"{image_name}_{int(time())}.json")
    output_image_path = os.path.join(config.DIRECTORIES["OUTPUT"], f"{image_name}.png")

    print(f"[*] Starting pipeline for: {input_image_filename}")

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