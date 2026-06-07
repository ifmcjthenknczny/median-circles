# /// script
# dependencies = ["pillow", "numpy"]
# ///
import sys, json, numpy as np
from PIL import Image
import config


def analyze(img_path, output_json_path, grid_size=config.GRID_SIZE):
    img = Image.open(img_path).convert("RGB")
    w, h = img.size
    cw, ch = w // grid_size, h // grid_size
    matrix = []
    for r in range(grid_size):
        row = []
        for c in range(grid_size):
            box = (
                c * cw,
                r * ch,
                (c + 1) * cw if c < grid_size - 1 else w,
                (r + 1) * ch if r < grid_size - 1 else h,
            )
            cell = np.array(img.crop(box))
            row.append(np.median(cell, axis=(0, 1)).astype(int).tolist())
        matrix.append(row)

    with open(output_json_path, "w") as f:
        json.dump(matrix, f)
    return output_json_path


if __name__ == "__main__":
    analyze(sys.argv[1], sys.argv[2])
