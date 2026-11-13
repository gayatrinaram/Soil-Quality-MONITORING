# RGB Field Image Explorer

An exploratory computer-vision project that processes a field image with OpenCV and NumPy, calculates a red-blue colour index, and displays a colour-mapped visualisation. It includes both a Google Colab notebook and a small Streamlit app.

> **Technical clarification:** This project does not calculate scientific NDVI. True NDVI requires red and near-infrared (NIR) reflectance bands. This project uses the red and blue channels of an ordinary RGB image as an exploratory proxy only. It does not measure soil quality, nutrients, moisture, or validated crop health.

## Try the project

- [Open the notebook in Google Colab](https://colab.research.google.com/github/gayatrinaram/Soil-Quality-MONITORING/blob/main/Soil_Quality_Monitoring.ipynb)
- [Portfolio website source](docs/index.html) — personal portfolio website hosted from this repository's `docs/` folder

## What it does

1. Accepts an uploaded field or aerial image.
2. Validates and reads the image with OpenCV.
3. Calculates the per-pixel index `(R - B) / (R + B)`.
4. Normalises the result for visualisation.
5. Applies a colour map to make spatial colour variation easier to inspect.
6. Provides a Streamlit interface for uploading an image and downloading the visualisation.

## Run locally

```bash
git clone https://github.com/gayatrinaram/Soil-Quality-MONITORING.git
cd Soil-Quality-MONITORING
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Upload a JPG, PNG, or TIFF image in the app.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Repository structure

```text
Soil-Quality-MONITORING/
├── app.py                         # Streamlit user interface
├── src/
│   └── rgb_index.py                # Reusable image-processing functions
├── tests/
│   └── test_rgb_index.py           # Unit tests
├── docs/                           # Personal portfolio website (GitHub Pages source)
│   ├── index.html
│   └── assets/
│       ├── css/style.css
│       └── js/main.js
├── Soil_Quality_Monitoring.ipynb   # Google Colab notebook
├── requirements.txt
└── README.md
```

## Tech stack

Python · OpenCV · NumPy · Streamlit · Pillow · Google Colab

## Limitations and next steps

- Results are sensitive to lighting, shadows, camera settings, and image content.
- The colour map is a visual aid, not a universal classification scale.
- A scientifically meaningful remote-sensing extension would use calibrated red and NIR bands, reflectance preprocessing, and ground-truth validation.
- Further improvements could include batch processing, image-quality checks, geospatial metadata support, and validated comparisons against field observations.

## Author

**Gayatri Naram** · [GitHub profile](https://github.com/gayatrinaram)
