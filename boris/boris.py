import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

logs = open("security.log").read()

def guess():
    # Create a DataFrame from the log data
    df = pd.DataFrame(logs, columns=["message", "label"])

    # Separate features (message) and labels (log type)
    X = df["message"]
    y = df["label"]

    # Convert log messages into numerical features using CountVectorizer
    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)

    # Split data into training and testing sets
    X_train_vec, X_test_vec, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

    # Create a Decision Tree classifier
    classifier = DecisionTreeClassifier(random_state=42)

    # Train the classifier
    classifier.fit(X_train_vec, y_train)

    # Make predictions on the test set
    y_pred = classifier.predict(X_test_vec)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print(y_pred)

print(logs)