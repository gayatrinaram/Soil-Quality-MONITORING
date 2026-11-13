# RGB Field Image Analysis

An exploratory computer-vision notebook that processes an uploaded field image with OpenCV and visualises a red-blue colour index.

[**Open the notebook in Google Colab**](https://colab.research.google.com/github/gayatrinaram/Soil-Quality-MONITORING/blob/main/Soil_Quality_Monitoring.ipynb)

## What it does

1. Accepts a user-uploaded field image.
2. Reads and validates the image with OpenCV.
3. Calculates the per-pixel red-blue index, `(R - B) / (R + B)`.
4. Normalises the index for visualisation.
5. Applies a colour map to make spatial colour variation easier to inspect.

## Technical clarification

**This notebook does not calculate scientific NDVI.** True NDVI requires red and near-infrared (NIR) reflectance bands. This project uses red and blue channels from a standard colour image as an exploratory visual proxy. It does not measure soil quality, nutrients, moisture, or validated crop health.

## Tech stack

- Python
- OpenCV
- NumPy
- Google Colab

## Run it

1. Open the Colab link above.
2. Run the notebook cells in order.
3. Upload a supported image when prompted.
4. Compare the original image with the colour-mapped index visualisation.

## Repository structure

```text
Soil-Quality-MONITORING/
├── Soil_Quality_Monitoring.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

## Limitations and future improvements

- Results are sensitive to lighting, shadows, camera settings, and image content.
- The colour map is a visual aid, not a universal classification scale.
- A scientifically meaningful remote-sensing extension would use calibrated red and NIR bands, reflectance preprocessing, and ground-truth validation.
- Additional improvements could include batch processing, saved output images, and automated image-quality checks.

## Author

**Gayatri Naram** · [GitHub](https://github.com/gayatrinaram)
