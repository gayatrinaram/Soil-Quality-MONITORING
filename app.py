"""Local Streamlit interface for exploratory RGB field-image visualisation."""
import streamlit as st
from PIL import Image
import numpy as np
import cv2
from src.rgb_index import analyse_image_bytes

st.set_page_config(page_title="RGB Field Image Explorer", page_icon="🌱", layout="wide")
st.title("RGB Field Image Explorer")
st.caption("An exploratory computer-vision demo using OpenCV and NumPy.")
st.warning(
    "This is NOT scientific NDVI. True NDVI requires red and near-infrared (NIR) "
    "reflectance bands. This RGB red-blue index is a visual experiment only; it "
    "does not measure soil quality or diagnose plant health."
)

uploaded = st.file_uploader("Upload a field or aerial image", type=["png", "jpg", "jpeg", "tif", "tiff"])
if uploaded:
    try:
        original = Image.open(uploaded).convert("RGB")
        index_map, colour_map = analyse_image_bytes(uploaded.getvalue())
        left, right = st.columns(2)
        with left:
            st.subheader("Original image")
            st.image(original, use_container_width=True)
        with right:
            st.subheader("RGB index visualisation")
            rgb_colour_map = cv2.cvtColor(colour_map, cv2.COLOR_BGR2RGB)
            st.image(rgb_colour_map, use_container_width=True)
        st.metric("Image dimensions", f"{original.width} × {original.height}")
        st.metric("Index range", f"{float(np.min(index_map)):.3f} to {float(np.max(index_map)):.3f}")
        ok, encoded = cv2.imencode(".png", colour_map)
        if ok:
            st.download_button(
                "Download visualisation",
                data=encoded.tobytes(),
                file_name="rgb-index-visualisation.png",
                mime="image/png",
            )
    except Exception as exc:
        st.error(f"Unable to process this image: {exc}")
else:
    st.info("Upload an image to explore its RGB colour variation.")

st.divider()
st.caption("Educational demonstration only. Outputs are sensitive to lighting, shadows, camera settings, and image content.")
