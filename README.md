# Butterfly and Moth Classification Model

![image](/readme_images/am-i-responsive.png)

Please view the deployed project [here]()

## Dataset
- The dataset was taken from [Kaggle](https://www.kaggle.com/datasets/gpiosenka/butterfly-images40-species).
- It provided 13,094 images of butterflies and moths, distributed among 100 different species.
- The dataset came with a train, test, validation set up but the ratios of the three folders was unnaceptable for the training of a CNN. I therefore retistributed the data to 70:20:10, respectively. 
- The folder names were also restructured to reflect the standard set up.

## Business Requirements
1. Determine the population distribution, based on current data.
2. Provide average image, image veriability, and image montage for each species classification as a quick reference for researchers in the field.
3. Create an ML model that can classify 100 different species of butterflys and moths with 75% accuracy; a high benchmark for such a complex model.

## Hypotheses and Validation of Hypotheses
- Present a visual average of each classification, and determine whether this can assist in educating researchers in collecting the data.
    - Given the variations in the image composition for each datapoint, the average image did not provide the required detail to researchers to use when trying to classify an image manually.
- Create an image montage of random selections of each classification, for reference.
    - Going forward, researchers will be able to use the dashboard to produce an image montage fo a selected species.

## ML Business Case
- The butterfly and moth classification model is to be used in classifying images of butterflies or moths provided by researchers and members of the public. The aim is to, over time, develop a strong understanding of species distribution and population over a specified area; the concern that brought this model to life was biodiversity but has obvious use cases for ecology and etemology requirements.
- The aim is to provide the model that can perform such tasks with an accuracy rate of 75%.
- The model output is a probability rating of each image belonging to each label (species).

## Model Description
- The Convolutional Neural Network (CNN) will be made up of 14 layers:
- Five pairs of convolutional and pooling layers.
- A single flatten layer.
- A dense layer followed by a dropout layer that will drop 30% of the nodes, to prevent overfitting.
- The output layer, which uses the softmax activation function, will output a probability for each image to belong to each class.
- The model is then complied, using the loss function categorical crossentropy, as is common with multiclass classification, the adam optimizer, and the accuracy metric.

## Model Development
- The model went through several iterations before it met the performance criteria.
- The 1st version contained:
    - Conv2D layers (32, 64, 64, 128).
    - Dropout rate of 30%.
    - Batch size of 20.
    - 20 epochs.
        - Accuracy: 66%
- The 2nd version contained:
    - Conv2D layers (32, 64, 64, 128, 256).
    - Dropout rate of 30%.
    - Batch size of 40.
    - 26 epochs.
        - Accuracy: 73%
- The 3rd version contained:
    - Conv2D layers (64, 64, 128, 128, 256).
    - Dropout rate of 30%.
    - Batch size of 35.
    - 32 epochs.
        - Accuracy: model accuracy did not improve between 1st and 4th epoch (1.5%)
- The 4th version contained:
    - Conv2D layers (32, 64, 128, 128, 256).
    - Dropout rate of 40%.
    - Batch size of 50.
    - 30 epochs.
        - Accuracy: 72%
- The 5th version contained:
    - Conv2D layers (32, 64, 64, 128, 256).
    - Dropout rate of 30%.
    - Batch size of 40.
    - 45 epochs.
        - Accuracy: 76%
- The 5th version of the model has been selected for use.
- After fitting it proported a loss of 0.9708, and a val_loss of 0.8476. The validation loss being lower than the training loss suggest the model is generalising well to new data.
- After fitting, the model proported an accuracy level of 0.7140 and a val_loss of 0.7648. The validation accuracy being at 76% on a 100 class classification problem is acceptable. For reference, random allocation would result in a sucess rate of 1%.

## Dashboard Design
- The dashboard design follows the basic set up of the walkthrough project.
#### Sidebar:
- The sidebar is made up of 5 radio buttons to navigate through the dashboard with.
![image](/readme_images/sidebar_dahboard.png)
#### Project Summary Page:
- Displays information about the use case for the ML model.
- Provides information about the dataset.
- Offers a link to the readme.md.
- Sates the business requirements.
![image](/readme_images/project_summary_dashboard.png)
#### Data Visualisation Page:
- Provides the option for a population distribution chart.
- Offers the user the ability to see the average image for each label.
- Creates an image montage for a selected species.
![image](/readme_images/dataset_visualiser_dashboard.png)
#### Species Classification Page:
- Allows users to input an image for classification.
- Also offers a potential dataset to draw from.
![image](/readme_images/ml_species_classification_tool.png)
#### Project Hypothesis and Validation Page:
- States the project hypothesises and how they were validated.
![image](/readme_images/hypothesis_dashboard.png)
#### ML Prediction Metrics Page:
- Shows a plot of label frequencies for train, test and validation sets.
![image](/readme_images/dataset_breakdown_dashboard.png)
- Lays out the history of the development of the model, including the perameters and hyperperameters of each.
![image](/readme_images/model_history_dashboard.png)
- Displays a plot of the model evaluation results.
![image](/readme_images/model_eval_dashboard.png)

## Technologies Used
#### Languages:
- Python
- Markdown
#### Platforms:
- Kaggle
- Jupyter Notebooks
- Heroku
#### Libraries:
- Tensor Flow
- Keras
- Pandas
- NumPy
- Plotly
- Seaborn
- Streamlit
- Matplotlib
- Scikit Learn

## CRISP-DM
- CRISP-DM stands for Cross-Industry Standard Process for Data Mining. It is a widely adopted methodology for data mining projects.
- Business Understanding:
 - The project objectives were to create a more robust and streamlined methodology for classifying butterfly and moth species.
 - This was to be achived with a CNN ML model that would automate the process of classification; and with visualisation tools of the given data.
- Data Understanding/Data Preparation:
 - The data was collected form a kaggle dataset.
 - The data was prepared for use in an ML model first by reformatting the directories to suit the required standard. 
 - Secondly, the data was redistributed to reflect a 70:20:10 ratio for train, test and validation sets, respectivley.
 - Thirdly, the data was visualised in terms of distribution between target variables.
- Modeling:
 - Given that this is a multiclass classification problem, the type of model chosen was a deep neural network.
 - The model was to be made up of a series of convolutional and pooling layer pairs, witha. flattern layer, a dense layer and a dense output layer. The intricacies of this are detailed in the model development section of this README.md document.
- Evaluation:
 - The model was evaluated in the context of the business requirement of a 75% accuracy rating. Thsi was deemed acceptable by industry standards for a classification model that features far less targets than 100, which this model does.
 - This standard was reached in the 5th version of the model, as detailed in the model development section of this README.md document.
 - Another metric by which the model was evaluated is it's accuracy compared to it's validation accuracy:
![image](/outputs/v1/model_accuracy.png)
 - The final metric by whcih the model's performance was evaluated was its loss compared to validation accuracy:
![image](/outputs/v1/model_loss.png)
 - As can be seen fromt he above graphs, the model was able to generalise it's training to predict on unseen data.
- Deployment:

## Credits
- Data Set is from Kaggle.
- The function to split the data was taken from the first walkthrough project.
- The function to load images as an array was taken from the first walkthrough project.
- The augmented image data variable was taken from the first walkthrough project.

## Acknowledgements 
 - Mo Shami, my mentor for the project was of great help when providing guidence and advice.
