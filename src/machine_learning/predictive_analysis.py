import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import os

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
from src.data_management import load_pkl_file

# def plot_predictions_probabilities(pred_proba, pred_class):
#     """
#     Plot prediction probability results
#     """

#     class_indices = load_pkl_file(file_path=f"outputs/v1/class_indices.pkl")


#     prob_per_class = pd.DataFrame(
#         data=np.zeros(len(class_indices)),
#         index=class_indices,
#         columns=['Probability']
#     )

#     for idx, cls in enumerate(pred_class):
#         prob_per_class.loc[cls, 'Probability'] = pred_proba.idx 

#     prob_per_class = prob_per_class.round(3)

#     prob_per_class['Species'] = prob_per_class.index

#     fig = px.bar(
#         prob_per_class,
#         x='Species',
#         y=prob_per_class['Probability'],
#         range_y=[0, 1],
#         width=600, height=300, template='seaborn')
#     st.plotly_chart(fig)


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """

    image_shape = load_pkl_file(file_path=f"outputs/v1/image_shape.pkl")
    print(image_shape)
    img_rgb = img.convert('RGB')
    

    img_resized = img_rgb.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image



def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    labels = os.listdir('inputs/butterfly_moth/images/validation')
    model = load_model(f"outputs/v1/butterfly_moth_classification_final.h5")

    predict_probabilities = model.predict(my_image)
    highest_prob = np.argmax(predict_probabilities, axis=1)

    prediction_index = highest_prob[0]
    prediction_class = labels[prediction_index]

    prediction_value = predict_probabilities[0,prediction_index]

    st.write(
        f"The predictive analysis indicates the species of butterfly is: "
        f"**{prediction_class.title().replace('_', ' ')}**")

    return predict_probabilities, prediction_class

