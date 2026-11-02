import streamlit as st
import pickle
from preprocessing import transform_message

tf_idf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('SMS/Email Spam Classifier')

inp_sms = st.text_area("Enter the message")

if st.button("Predict"):

    #1. Preprocessor
    transformed_mssg =transform_message(inp_sms)

    #2. Vectorizer
    vec_inp = tf_idf.transform([transformed_mssg])

    #3. Predict
    prediction = model.predict(vec_inp)[0]

    #4. Display Result
    if prediction == 1:
        st.error("Spam Message Detected")
    else:
        st.success("Message is not spam")