import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate import load_test_evaluation


def ml_prediction_metrics_body():

    st.write('## Train, Validation and Test Set: Labels Frequencies')

    labels_distribution = plt.imread(f'outputs/v1/dataset_breakdown.png')
    st.image(labels_distribution, caption='Dataset Breakdown')

    st.write('## Model History')
    st.write(
        f'The model went through 5 versions before meeting the criteria '
        f'expected for the business case.'
    )
    st.warning('### Version One:')
    st.markdown('Conv2D layers (32, 64, 64, 128)')
    st.markdown('Dropout rate of 30%')
    st.markdown('Batch size of 20')
    st.markdown('20 epochs')
    st.markdown('Accuracy: 60%')

    st.warning('### Version Two:')
    st.markdown('Conv2D layers (32, 64, 64, 128, 256)')
    st.markdown('Dropout rate of 30%')
    st.markdown('Batch size of 40')
    st.markdown('26 epochs')
    st.markdown('Accuracy: 73%')

    st.warning('### Version Three:')
    st.markdown('Conv2D layers (64, 64, 128, 128, 256)')
    st.markdown('Dropout rate of 30%')
    st.markdown('Batch size of 35')
    st.markdown('32 epochs')
    st.markdown('Accuracy: Early stop prevented training moving past 4th Epoch.')

    st.warning('### Version Four:')
    st.markdown('Conv2D layers (32, 64, 128, 128, 256)')
    st.markdown('Dropout rate of 40%')
    st.markdown('Batch size of 50')
    st.markdown('30 epochs')
    st.markdown('Accuracy: 72%')

    st.success('### Version Five:')
    st.markdown('Conv2D layers (32, 64, 64, 128, 256)')
    st.markdown('Dropout rate of 30%')
    st.markdown('Batch size of 40')
    st.markdown('45 epochs')
    st.markdown('Accuracy: 76%')
    st.markdown(
        f'After fitting it proported a loss of 0.9708, and a val_loss of 0.8476. \n'
        f'The validation loss being lower than the training loss suggest the model is \n'
        f'generalising well to new data.\n After fitting, the model proported an \n'
        f'accuracy level of 0.7140 and a val_loss of 0.7648. The validation accuracy being '
        f'at 76% on a 100 class classification problem is acceptable. For reference, '
        f'random allocation would result in a sucess rate of 1%.'
    )

    st.write('## Model Evaluation')

    model_loss = plt.imread(f'outputs/v1/model_loss.png')
    st.image(model_loss, caption='Model Version 5 Loss Graph')

    model_loss = plt.imread(f'outputs/v1/model_accuracy.png')
    st.image(model_loss, caption='Model Version 5 Accuracy Graph')
    