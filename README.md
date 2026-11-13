# RGB Vegetation Index Visualisation

A small computer-vision notebook that accepts an uploaded field image, processes it with OpenCV, calculates a red–blue normalized-difference score, and visualises the result as a colour-mapped image.

> **Technical note:** The current notebook does not calculate scientific NDVI. True NDVI requires near-infrared (NIR) and red reflectance bands. This implementation uses the red and blue channels of a standard image as a visual proxy, so its output should not be interpreted as a validated vegetation-health or soil-quality measurement.

## Project overview

The notebook demonstrates an image-processing workflow:

1. Upload a field or aerial image in Google Colab.
2. Read the image with OpenCV.
3. Split the image into colour channels.
4. Calculate the normalised red–blue difference, `(R - B) / (R + B)`.
5. Handle invalid numerical values and normalise the result for display.
6. Apply an OpenCV colour map to make spatial patterns easier to inspect.

## Technologies

- Python
- OpenCV
- NumPy
- Google Colab

## Run the notebook

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gayatrinaram/Soil-Quality-MONITORING/blob/main/Soil_Quality_Monitoring.ipynb)

1. Open the notebook in Google Colab.
2. Run the import and upload cell.
3. Upload a suitable field image when prompted.
4. Review the original image and the colour-mapped output.

## Repository contents

- `Soil_Quality_Monitoring.ipynb` — interactive image-processing notebook.

## Current scope and limitations

- This is an exploratory image-visualisation exercise, not a calibrated remote-sensing pipeline.
- Standard RGB imagery does not contain a dedicated NIR band.
- The red–blue proxy is sensitive to lighting, camera settings, shadows, and image content.
- The notebook does not measure soil nutrients, pH, moisture, or other soil properties.
- The colour map is a visual aid; it is not a scientific classification by itself.

## Potential next steps

- Support multispectral imagery with explicit red and NIR band inputs to calculate true NDVI.
- Add image validation, reusable functions, and configurable output visualisation.
- Compare outputs against ground-truth observations before making agricultural interpretations.

## Author

**Gayatri Naram**  
[GitHub profile](https://github.com/gayatrinaram)

---

This project is shared as an educational computer-vision demonstration. It is not intended for agronomic, environmental, or scientific decision-making without validation.
