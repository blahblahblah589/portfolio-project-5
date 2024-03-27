import streamlit as st
import matplotlib.pyplot as plt


def project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"Despite varying species of butterfly and moth sharing both \n"
        f"obvious (such as shape) and non-obvious (such as wing patterns), \n"
        f"the ML model uses it's neural network structure to differentiate between \n"
        f"100 different species with a high success rate. \n\n The use of an "
        f"image montage will alow the human researchers a reliable and quick"
        f"subset of image data, with which to reference when needed.\n\n Average "
        f"Image, Variability Image unfortunately did not present as a useful tool."
    )