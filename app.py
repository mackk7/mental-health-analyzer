import streamlit as st
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import re
import string
import demoji

# --- MODEL & TOKENIZER LOADING ---
@st.cache_resource
def get_model():
    tokenizer = DistilBertTokenizer.from_pretrained("./my_model")
    model = DistilBertForSequenceClassification.from_pretrained("./my_model")
    return tokenizer, model

tokenizer, model = get_model()

# --- PREPROCESSING FUNCTION (Must be identical to the one in the notebook) ---
demoji.download_codes()
def preprocess_text(text):
    text = text.lower()
    text = demoji.replace_with_desc(text, sep=" ")
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# --- STREAMLIT UI ---
st.set_page_config(page_title="Mental Health Analyzer", page_icon="🧠", layout="centered")

st.title("🧠 Mental Health Text Analyzer")
st.markdown("Enter a piece of text (like a journal entry or a post) to analyze its emotional tone for signs of potential distress. This is not a diagnostic tool.")

user_input = st.text_area("Enter your text here:", height=150)

if st.button("Analyze"):
    if user_input:
        # 1. Preprocess the input
        cleaned_text = preprocess_text(user_input)

        # 2. Tokenize the text
        inputs = tokenizer(cleaned_text, return_tensors="pt", truncation=True, padding=True, max_length=128)

        # 3. Get model prediction
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits

        # 4. Convert logits to probabilities and get the prediction
        probabilities = torch.softmax(logits, dim=1)
        # prediction = torch.argmax(probabilities, dim=1).item()
        # --- NEW, SAFER LOGIC ---
        suicide_prob = probabilities[0][1].item() # Assuming '1' is the suicidal class
        if suicide_prob > 0.20: # Set a low threshold of 20%
            prediction = 1 # Flag as potential suicide post
        else:
            prediction = 0
        confidence = probabilities[0][prediction].item()

        # Define labels
        labels = {0: "Not a Suicide post", 1: "Potential Suicide post"}
        result = labels[prediction]

        # 5. Display the result
        st.subheader("Analysis Result")
        if prediction == 1:
            st.error(f"**Status:** {result}")
            st.warning("Suggestion: It looks like you might be going through a tough time. Please consider talking to someone you trust, like a friend, family member, or a professional. You are not alone.")
        else:
            st.success(f"**Status:** {result}")
            st.info("Suggestion: Keep expressing yourself! Regular self-reflection is a great habit for maintaining mental well-being.")

        st.write(f"**Confidence:** {confidence:.2%}")

    else:
        st.warning("Please enter some text to analyze.")

# --- ETHICAL DISCLAIMER ---
st.markdown("---")
st.warning(
    """
    **Disclaimer:** This AI is an experimental tool and **not a substitute for professional medical advice**. 
    If you are in distress, please seek help from a qualified healthcare provider or a mental health professional.
    """
)