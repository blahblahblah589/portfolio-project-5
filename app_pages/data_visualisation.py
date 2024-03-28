import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def data_visualisation_body():
    st.write('## Dataset Visualiser')
    st.info(
        f'* The client is wants an average image per class to determine\n '
        f'if the results could help researchers recognise species.')
    
    version = 'v1'
    labels = os.listdir('inputs/butterfly_moth/images/test')
    if st.checkbox('Average Image'):
        label_to_display = st.selectbox(label="Select species", options=labels, index=0)
        if st.button("Create Average Image"):
            average_image_display(label_to_display=label_to_display)

    
    st.warning(
        f'We notice the average and variability images did not show '
        f'patterns where we could intuitively differentiate one from another.'
        )

    if st.checkbox("Image Montage"): 
      st.write("* To refresh the montage, click on the 'Create Montage' button")
      my_data_dir = 'inputs/butterfly_moth/images'
      labels = os.listdir('inputs/butterfly_moth/images/test')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create Montage"):      
        create_image_montage(data=labels,
                      label_to_display=label_to_display,
                      nrows=3, ncols=3, figsize=(25,10))
      st.write("---")

    if st.checkbox("Population Distribution"):
        population_distribution(data='inputs/butterfly_moth/images/test')
        st.write("---")


def average_image_display(label_to_display):

    avg_image = plt.imread(f'outputs/v1/avg_var_{label_to_display}.png')
    st.image(avg_image, caption=f'Average Image and Average Variance for {label_to_display}')

def create_image_montage(data, label_to_display, nrows, ncols, figsize):
    
    labels = os.listdir('inputs/butterfly_moth/images/test')
    if label_to_display in labels:
        montage = os.listdir('inputs/butterfly_moth/images/test' + '/' + label_to_display)
        if nrows * ncols < len(montage):
            img_index = random.sample(montage, nrows * ncols)
        else:
            print('Error - not enough images for montage.')
            print('Please decrease "ncols" or "nrows".')

    montage_rows = range(0, nrows)
    montage_cols = range(0, ncols)
    montage_plot = list(itertools.product(montage_rows, montage_cols))

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for x_images in range(0, nrows * ncols):
        img = imread('inputs/butterfly_moth/images/test' + '/' + label_to_display + '/' + img_index[x_images])
        img_shape = img.shape
        fig.suptitle((f'{label_to_display.replace("_"," ").title()}'))
        axes[montage_plot[x_images][0], montage_plot[x_images][1]].imshow(img)
    plt.tight_layout()
    st.pyplot(fig=fig)

def population_distribution(data):

    image_data = []
    data = ('inputs/butterfly_moth/images/test')
    labels = os.listdir('inputs/butterfly_moth/images/test')
    for label in labels:
        species = os.path.join(data, label)
        count = len([name for name in os.listdir(species) if os.path.isfile(os.path.join(species, name))])

        image_data.append({'Species': label, 'Recorded Population': count})

    species_df = pd.DataFrame(image_data)
    total_population = species_df['Recorded Population'].sum()

    print(species_df)
    print(f'Total Recorded Population: {total_population}')

    population = species_df['Recorded Population']
    species = species_df['Species']

    plt.figure(figsize=(40,12))
    plt.bar(species, population, color='green')
    plt.ylim(ymin=5)
    plt.xlabel('Species')
    plt.ylabel('Population')
    plt.title('Population Distribution')
    plt.xticks(rotation=90)
    st.pyplot(plt)