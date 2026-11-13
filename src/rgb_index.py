"""Exploratory RGB red-blue image index utilities.

This is not NDVI: true NDVI requires red and near-infrared reflectance bands.
"""
from __future__ import annotations
import cv2
import numpy as np


def calculate_rgb_red_blue_index(image: np.ndarray) -> np.ndarray:
    """Calculate (R - B) / (R + B) for a three-channel OpenCV BGR image."""
    if image is None or not isinstance(image, np.ndarray):
        raise ValueError("image must be a valid NumPy array")
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("Expected a three-channel colour image")
    channels = image.astype(np.float32)
    blue, _, red = cv2.split(channels)
    denominator = red + blue
    result = np.zeros_like(denominator, dtype=np.float32)
    np.divide(red - blue, denominator, out=result, where=denominator != 0)
    return np.nan_to_num(result, nan=0.0, posinf=0.0, neginf=0.0)


def colourise_index(index_map: np.ndarray) -> np.ndarray:
    """Normalise an index map and return an OpenCV JET colour visualisation."""
    if index_map is None or not isinstance(index_map, np.ndarray) or index_map.ndim != 2:
        raise ValueError("index_map must be a two-dimensional NumPy array")
    scaled = cv2.normalize(index_map, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    return cv2.applyColorMap(scaled, cv2.COLORMAP_JET)


def analyse_image_bytes(image_bytes: bytes) -> tuple[np.ndarray, np.ndarray]:
    """Decode image bytes and return (index_map, colourised_map)."""
    if not image_bytes:
        raise ValueError("No image data provided")
    encoded = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(encoded, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Could not decode image; upload a valid image file")
    index_map = calculate_rgb_red_blue_index(image)
    return index_map, colourise_index(index_map)
