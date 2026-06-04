# Median Circles

A modular Python toolset designed to analyze an image's color distribution and generate a minimalist geometric representation. The project is built with **decoupling** in mind, separating data analysis from image rendering.

## 🏗 Architecture

The project consists of three main components:

1. **`analyzer.py`**: Extracts the median color from a 5x5 grid of the source image. Outputs raw JSON data to `stdout`.
2. **`visualizer.py`**: Consumes color data and renders a 5x5 grid of circles on a white canvas.
3. **`orchestrator.py`**: The "brain" that manages the pipeline, piping data between the analyzer and the visualizer without using intermediate files.

## 🚀 Getting Started

This project uses **[uv](https://github.com/astral-sh/uv)** for seamless dependency management. You don't need to manually install `Pillow` or `numpy` in your global environment.

### Prerequisites

* Python 3.12+
* `uv` installed (`curl -LsSf https://astral-sh.uv.run/install.sh | sh`)

### Usage

To run the entire pipeline, simply execute the orchestrator and provide the path to your source image:

```bash
python orchestrator.py <image_filename>.<image_extension>

```

## 🛠 Script Details

### 1. Analyzer (`analyze.py`)

Calculates the median RGB value for each cell in a 5x5 grid.

* **Input**: Image file path.
* **Output**: JSON array of RGB tuples via `stdout`.

### 2. Visualizer (`visualize.py`)

Renders a high-resolution (1000x1000px) image.

* **Input**: JSON string of colors, output filename.
* **Output**: A `.png` file featuring colored circles on a white background.

### 3. Orchestrator (`orchestrator.py`)

The glue code that uses `subprocess` to run the scripts.

* Ensures that dependencies for each script are handled by `uv run`.
* Handles the data flow via memory pipes.
* Logs the final absolute path of the generated image.

## 🎨 Example Output

The pipeline transforms a standard photograph into a clean, 5x5 dot-matrix representation:

* **Step 1**: Source Image → 25 Median Color Points (JSON).
* **Step 2**: JSON → `output/<timestamp>.png` (Minimalist Grid).

## 📜 License

MIT - Feel free to use and modify for your own projects.

---

### Pro-tip:

Since the scripts use `uv` inline metadata, you can also run them individually for testing:

```bash
uv run analyze.py image.jpg

```

## License

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

## Contact

For questions or feedback, please reach out via GitHub.
[ifmcjthenknczny](https://github.com/ifmcjthenknczny)  

Project Link: [https://github.com/ifmcjthenknczny/median-circles](https://github.com/ifmcjthenknczny/median-circles)