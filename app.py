import streamlit as st
from function.datapreprocessing import DataPreprocessing
from function.User_file import User
import streamlit.components.v1 as components
from function.UserDao_file import UserDao
from keras.models import load_model
import numpy as np

dp = DataPreprocessing("./data/data_processed/trainprocessed.csv","./data/data_processed/generate.csv")

# Function to predict sentiment
def predict_sentiment(comment):
    model_sentiment = load_model("./model/model_sentiment_lstm.h5")
    result = model_sentiment.predict(comment)
    label_index = np.argmax(result, axis=1)
    predicted_label = dp.labelEn.inverse_transform(label_index)
    return predicted_label

# Function to generate text
def generate_text(comment):
    model_generate = load_model("./model/model_lstm_generate_text.h5")
    temp=""
    for _ in range(3):
        comment_processed = dp.fit_transform_generate(comment)
        predicted_probs = model_generate.predict(comment_processed)
        word = dp.generate.index_word[np.argmax(predicted_probs)]
        comment += " " + word
        temp += " " +word
    return temp

# Streamlit app for sentiment analysis
def sentiment_analysis(username):
    st.title("Vietnamese Sentiment Analysis")
    user_id = User(username)
    userDao = UserDao()
    if userDao.get_user_id(user_id) == 1:
        st.write("Hello, admin")
        if st.button("Predict"):
            comment_of_user = userDao.get_comment_by_user()
            for comment in comment_of_user:
                processed_comment = dp.fit_transform(comment[0].lower())
                full_name = userDao.get_full_name(User(comment=comment[0]))
                prediction = predict_sentiment(processed_comment)
                prediction = dp.Standardization(prediction)
                st.write(f"Hello {full_name},! This is the result of analyzing the results of the comment")
                st.write(f"'{comment[0]}'")
                st.write("Sentiment:", prediction)
    else:
        comment_state = st.empty()
        comment_input = st.text_area("Enter your comment:", key='comment_area')
        st.write(f"Hello, {username}")
        space_key_js = """
        <script>
        document.addEventListener("keydown", function(event) {
            var commentInput = document.querySelector('textarea[key="comment_area"]');
            if (event.code === "Space") {
                return true;
                }
            }
        });
        </script>
        """
        space_key_event = components.html(space_key_js, height=0)
        if st.button("Enter comment"):
            userDao.insert_comment(user_id, comment_input)
            st.success("Comment posted successfully!")  
        if space_key_event :
            updated_comment = generate_text(comment_input)
            comment_state.text(comment_input + updated_comment)

                
# Streamlit app for login page
def login_page():
    st.title("Login Page")
    username = st.text_input("Username:", key="username_input")
    password = st.text_input("Password:", type="password", key="password_input")
    user = User(username, password)
    userDao = UserDao()
    if st.button("Login"):
        login_success = userDao.check_login(user)
        if login_success == 1:
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
