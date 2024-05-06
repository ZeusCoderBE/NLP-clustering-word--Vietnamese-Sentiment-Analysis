import streamlit as st
from tensorflow.keras.models import load_model
from pyvi import ViTokenizer
import numpy as np
import datapreprocessing.datapreprocessing as pre
from sklearn.preprocessing import LabelEncoder

# Load the pre-trained model
model = load_model("./model/model_sentiment_lstm.h5")

# Load and preprocess the training data
x_train, y_train = pre.ReadData("DataPhone/trainprocessed.csv")
x_train = pre.wordseparation(x_train)
x_train_corpus = pre.CreateCorpus(x_train)  

# Function to preprocess the user input
def preprocess_comment(comment):
    comment = pre.remove_pucntuation(comment)
    comment = pre.remove_stopword(comment)
    comment = [ViTokenizer.tokenize(comment)]
    separated_meaningful_words = pre.wordseparation(comment)
    return pre.Padding(separated_meaningful_words, x_train_corpus)

# Function to predict sentiment
def predict_sentiment(comment):
    label_encoder = LabelEncoder()
    label_encoder.fit_transform(y_train)
    result = model.predict(comment)
    label_index = np.argmax(result, axis=1)
    predicted_label = label_encoder.inverse_transform(label_index)
    return predicted_label

# Streamlit app
def main():
    st.title("Vietnamese Sentiment Analysis")
    comment = st.text_area("Enter your comment:")
    
    if st.button("Predict"):
        # Preprocess the user input
        processed_comment = preprocess_comment(comment)
        
        # Predict sentiment and display the result
        prediction = predict_sentiment(processed_comment)
        prediction = pre.Standardization(prediction)
        st.write("Sentiment:", prediction)

# Run the Streamlit app
if __name__ == "__main__":
    main()
