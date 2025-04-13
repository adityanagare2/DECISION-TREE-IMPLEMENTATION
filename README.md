# DECISION-TREE-IMPLEMENTATION
COMPANY: CODTECH IT SOLUTIONS 

NAME: Aditya Nagare

INTERN ID: CT12WH88 

DOMAIN: Machine Learning

DURATION: 12 weeks 

MENTOR: NEELA SANTOSH

## DESCRIPTION OF TASK
  #Project Description: 
Decision Tree Classifier Using Scikit-learn
As part of my machine learning internship, I was assigned the task of building and analyzing a Decision Tree classifier using Python and scikit-learn. The goal of this project was to learn how to implement a basic yet powerful classification model, visualize its logic, and understand how different features contribute to predictions. I chose the Iris dataset for this task because it is clean, well-structured, and commonly used in introductory machine learning projects. It contains features related to flower measurements and targets representing species labels, making it ideal for classification.


  #Tools & Technologies Used
Python: The programming language used for writing the entire project. It’s widely adopted in data science and machine learning for its simplicity and large number of libraries.

Pandas: Used for data manipulation and handling tabular data (like CSV-style tables). It helped in organizing and viewing the dataset.

Matplotlib & Seaborn: These two libraries were used to visualize the dataset and model insights. Seaborn was helpful in plotting relationships between features, and Matplotlib was used to display the decision tree structure and feature importance.

Scikit-learn (sklearn): The most critical tool used. Scikit-learn is a powerful Python library for machine learning. It provides easy-to-use methods for splitting data, building models (like Decision Trees), evaluating performance, and visualizing the decision-making process of models.



  #Implementation Summary
The project was implemented step-by-step to simulate a real-world machine learning workflow:

Data Loading:
I started by importing the built-in Iris dataset from scikit-learn. It includes 150 rows and 4 features (sepal length, sepal width, petal length, and petal width), along with target values representing three species of Iris flowers.

Data Visualization:
Before building the model, I used seaborn.pairplot to visualize how different features relate to one another. This helps get a sense of which features might be more useful for prediction.

Data Splitting:
The dataset was split into a training set (80%) and a test set (20%) using train_test_split. This ensures the model is evaluated on unseen data, helping assess real-world performance.

Model Training:
A DecisionTreeClassifier was initialized and trained on the training data. This algorithm works by splitting the data into smaller and smaller groups using simple decision rules, such as "Is petal length > 2.5 cm?".

Model Evaluation:
Predictions were made on the test set, and the model’s performance was measured using accuracy and a classification report. The model achieved over 95% accuracy without any tuning, showing strong results even with default settings.

Model Visualization:
I used plot_tree to visually show how the decision tree splits the data. This makes it easy to understand how the model makes decisions. I also plotted feature importance to see which measurements had the biggest impact on predictions.

Written Analysis:
Finally, I included a natural-language summary of what I observed: which features were most important, how accurate the model was, and how it might be improved in the future (e.g., pruning the tree or limiting depth).

  #Real-World Applications
Although this was a learning project, Decision Trees are used in many real-world applications:

Healthcare: Diagnosing diseases based on symptoms and test results.

Finance: Predicting whether a loan applicant is likely to default.

Retail: Determining which customers are likely to buy a product.

Education: Predicting student performance or dropout risks.

Agriculture: Classifying types of crops based on soil and climate data.

Decision Trees are especially useful when explainability is important. Because they resemble flowcharts, it's easy to understand how a decision was made, which is essential in fields like healthcare or legal decision-making.

##OUTPUT

![Image](https://github.com/user-attachments/assets/b0aa0aa4-fab9-4a58-80ee-39412a479de2)

![Image](https://github.com/user-attachments/assets/e4d2db1f-f3b9-4ff6-be5f-758a30be14c5)

![Image](https://github.com/user-attachments/assets/41c9b7ff-f4d1-419d-9531-053ea68658c6)

![Image](https://github.com/user-attachments/assets/7e8cb3b9-a6e9-4777-99ba-04810693ae81)

![Image](https://github.com/user-attachments/assets/189f8fde-2b6b-44d9-ac2f-d9021ddf2a17)
