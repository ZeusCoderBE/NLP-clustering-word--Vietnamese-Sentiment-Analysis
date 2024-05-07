import streamlit as st
from function import CRUD as execute
from keras.models import load_model
from pyvi import ViTokenizer
import numpy as np
from function import datapreprocessing as pre
from sklearn.preprocessing import LabelEncoder


# Load and preprocess the training data
x_train, y_train = pre.ReadData("./DataPhone/trainprocessed.csv")
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
    model = load_model("./model/model_sentiment_lstm.h5")
    result = model.predict(comment)
    label_index = np.argmax(result, axis=1)
    predicted_label = label_encoder.inverse_transform(label_index)
    return predicted_label

# Streamlit app for sentiment analysis
def sentiment_analysis(username):
    st.title("Vietnamese Sentiment Analysis")
    if execute.get_user_id(username)==1:
        st.write("Hello, admin")
        if st.button("Predict"):
            comment_of_user= execute.get_comment_by_user()
            for comment in comment_of_user:
                processed_comment = preprocess_comment(comment[0].lower())
                full_name=execute.get_full_name(comment[0])
                print(comment[0])
                prediction = predict_sentiment(processed_comment)
                prediction = pre.Standardization(prediction)
                st.write(f"Hello {full_name},! This is the result of analyzing the results of the comment")
                st.write(f"'{comment[0]}'")
                st.write("Sentiment:", prediction)
    else:
        comment = st.text_area("Enter your comment:")
        st.write(f"Hello, {username}")
        if st.button("Enter comment"):
            execute.insert_comment(username, comment)
            st.success("Comment posted successfully!")
# Streamlit app for login page
def login_page():
    st.title("Login Page")
    username = st.text_input("Username:", key="username_input")
    password = st.text_input("Password:", type="password", key="password_input")

    if st.button("Login"):
        login_success = execute.check_login(username, password)
        if login_success==1:
            st.session_state.page = "sentiment_analysis"
            st.session_state.username = username
        else:
            st.error("Invalid username or password.")
    else:
        st.info("Please login to access the sentiment analysis page.")

# Run the Streamlit app
if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "login"
    if "username" not in st.session_state:
        st.session_state.username = ""
    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "sentiment_analysis":
        sentiment_analysis(st.session_state.username)
