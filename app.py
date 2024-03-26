import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.project_summary import project_summary_body
from app_pages.data_visualisation import data_visualisation_body
from app_pages.species_classification import species_classification_body
from app_pages.project_hypothesis_validation import project_hypothesis_body
from app_pages.ml_prediction_metrics import ml_prediction_metrics_body

app = MultiPage(app_name='Butterfly and Moth Classification')

app.add_page('Project Summary', project_summary_body)
app.add_page('Data Visualisation', data_visualisation_body)
app.add_page('Species Classification', species_classification_body)
app.add_page('Project Hypothesis and Validation', project_hypothesis_body)
app.add_page('Machine Learning Prediction Metrics', ml_prediction_metrics_body)

app.run()