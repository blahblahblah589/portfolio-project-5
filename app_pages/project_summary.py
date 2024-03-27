import streamlit as st

def project_summary_body():

    st.write('# Project Summary')

    st.info(
        f'**General Information**\n\n'
        f'In recent year due to a litany of factors, '
        f'insect populations have decreased rapidly.\n'
        f'Ecologists and etymologists have been working '
        f'to collect as much data on the population of '
        f'various butterfly and moth species in the hope '
        f'to catalogue the decline as they look for a solution.\n'
        f'Currently the species classification is done manually by '
        f'a handful of researchers. The level of human error '
        f'as well as the time consumption of this task are both very high.\n'
        f'The aim of this project is to automate the process and in turn, '
        f'reduce the time consumption and human error.\n\n'
        f'**Dataset Information**\n\n'
        f'The dataset was taken from Kaggle. It consists of 13,094 '
        f'images of butterflies and moths, distributed among 100 different species.\n'
        f'The dataset came with a train, test, validation set up '
        f'but the ratios of the three folders was unacceptable for the training '
        f'of a CNN. I therefore redistributed the data to 70:20:10, respectively.'
    )

    st.write(
        f'* For additional information, please visit and **read** the '
        f'[Project README file](https://github.com/blahblahblah589/portfolio-project-5/blob/main/README.md).'
    )

    st.success(
        f'The project has 3 business requirements:\n'
        f'* 1 - Determine the population distribution, based on current data.\n'
        f'* 2 - Provide average image, image variability, and image montage for '
        f'each species classification as a quick reference for researchers in the field.\n'
        f'* 3 - Create an ML model that can classify 100 different species of butterflies \n'
        f'and moths with 75% accuracy.'
    )
 
