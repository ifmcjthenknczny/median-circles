# /// script
# dependencies = ["pillow"]
# ///
import sys, json
from PIL import Image, ImageDraw
import config

def render(json_file_path, output_path):
    with open(json_file_path, "r") as f:
        matrix = json.load(f)
        
    grid_size = len(matrix)
    cell_size, margin = config.CELL_SIZE, config.MARGIN
    canvas_size = grid_size * cell_size
    
    img = Image.new('RGB', (canvas_size, canvas_size), 'white')
    draw = ImageDraw.Draw(img)

    for r, row in enumerate(matrix):
        for c, color in enumerate(row):
            x0, y0 = c*cell_size + margin, r*cell_size + margin
            x1, y1 = (c+1)*cell_size - margin, (r+1)*cell_size - margin
            draw.ellipse([x0, y0, x1, y1], fill=tuple(color))

    img.save(output_path)

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])