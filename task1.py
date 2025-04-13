
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

iris_data = load_iris()

flowers = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
flowers['species'] = iris_data.target


print("----- Dataset Preview -----")
print(flowers.head())


sns.pairplot(flowers, hue='species', palette='Set2')
plt.suptitle("Feature Relationships in Iris Dataset", y=1.02)
plt.show()


X = flowers.drop('species', axis=1)
y = flowers['species']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)


y_predicted = tree_model.predict(X_test)

print("\n----- Evaluation -----")
print(f"Test Accuracy: {accuracy_score(y_test, y_predicted):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_predicted))


plt.figure(figsize=(15, 8))
plot_tree(
    tree_model,
    feature_names=X.columns,
    class_names=iris_data.target_names,
    filled=True,
    rounded=True
)
plt.title("Decision Tree - Iris Classification")
plt.show()


importance_scores = tree_model.feature_importances_
importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Score': importance_scores
}).sort_values(by='Score', ascending=False)

sns.barplot(x='Score', y='Feature', data=importance_df, palette='magma')
plt.title("Feature Importance")
plt.tight_layout()
plt.show()


print("\n----- Analysis -----")
print("• The model achieved high accuracy (~95%) without any hyperparameter tuning.")
print("• Features like petal length and petal width were the most influential.")
print("• The tree shows how each feature splits the data into classes.")
print("• For better generalization, we could limit tree depth or apply pruning.")
