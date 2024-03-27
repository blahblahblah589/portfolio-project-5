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
    st.write('# Dataset Visualiser')
    st.info(
        f'* The client is wants an average image per class to determine\n '
        f'if the results could help researchers recognise species.')
    
    version = 'v1'
    labels = os.listdir('inputs/butterfly_moth/images/validation')
    if st.checkbox('Average Image'):
        for label in labels:
            avg_image = plt.imread(f'outputs/{version}/avg_var_{label}.png')
    
    st.warning(
        f'We notice the average and variability images did not show '
        f'patterns where we could intuitively differentiate one from another.'
        )

    if st.checkbox("Image Montage"): 
      st.write("* To refresh the montage, click on the 'Create Montage' button")
      my_data_dir = 'inputs/butterfly_moth/images'
      labels = os.listdir('inputs/butterfly_moth/images/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create Montage"):      
        create_image_montage(data=labels,
                      label_to_display=label_to_display,
                      nrows=3, ncols=3, figsize=(10,25))
      st.write("---")

    if st.checkbox("Population Distribution"):
        population_distribution(data='inputs/butterfly_moth/images/validation')
        st.write("---")


def create_image_montage(data, label_to_display, nrows, ncols, figsize):
    
    labels = os.listdir('inputs/butterfly_moth/images/validation')
    if label_to_display in labels:
        montage = os.listdir('inputs/butterfly_moth/images/validation' + '/' + label_to_display)
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
        img = imread('inputs/butterfly_moth/images/validation' + '/' + label_to_display + '/' + img_index[x_images])
        img_shape = img.shape
        fig.suptitle((f'{label_to_display.replace("_"," ").title()}'))
        axes[montage_plot[x_images][0], montage_plot[x_images][1]].imshow(img)
    plt.tight_layout()
    plt.show()

def population_distribution(data):

    image_data = []
    data = ('inputs/butterfly_moth/images/validation')
    labels = os.listdir('inputs/butterfly_moth/images/validation')
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

    plt.figure(figsize=(25,10))
    plt.bar(species, population, color='green')
    plt.ylim(ymin=60)
    plt.xlabel('Species')
    plt.ylabel('Population')
    plt.title('Population Distribution')
    plt.xticks(rotation=90)
    plt.show()