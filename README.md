# 🧠 Mental Health Analyzer from Text

An AI-powered web application that analyzes written text to detect potential signs of mental distress, built with HuggingFace Transformers and Streamlit.

---

Note: The original trained model file was large and excluded due to GitHub file size limits.
The deployed Streamlit app demonstrates the final working version with the model hosted externally.

## 🚀 Live Demo

*[[Link to my deployed Streamlit App](https://mental-health-analyzer-f4wrt6kvq2qt6tt8vbcu2a.streamlit.app/)]* 



*[Screenshot of my running application here]*
## 📸 Screenshot<img width="1842" height="938" alt="Screenshot 2025-10-16 224020" src="https://github.com/user-attachments/assets/7896a1f9-31bb-4794-8bbe-c686e549970d" />

## 🎯 Problem Statement

In a world where many hesitate to discuss mental health openly, their written text often reflects their inner state. This project aims to build a tool that can analyze text from social media posts, chats, or journals to identify early signs of stress, anxiety, or depression, enabling timely support.

## ✨ Features

-   **NLP Analysis:** Utilizes a fine-tuned DistilBERT model to perform sentiment and emotional tone classification.
-   **Real-time Prediction:** Provides an immediate classification of the text into categories like "Potential Suicide post" or "Not a Suicide post".
-   **Confidence Score:** Displays the model's confidence in its prediction.
-   **Simple UI:** A clean and intuitive web interface built with Streamlit for easy use.

## 🛠️ Tech Stack

-   **Backend & ML:** Python, Pandas, scikit-learn
-   **Deep Learning:** PyTorch, HuggingFace Transformers (DistilBERT)
-   **Web Framework:** Streamlit
-   **Deployment:** Streamlit Community Cloud

## ⚙️ How to Run Locally

1.  Clone the repository:
    `git clone "https://github.com/mackk7/mental-health-analyzer.git"`
2.  Create and activate a virtual environment.
3.  Install dependencies:
    `pip install -r requirements.txt`
4.  Run the Streamlit app:
    `streamlit run app.py`

---

### ⚠️ Ethical Disclaimer

This project is an academic experiment and is **not a diagnostic tool**. It is not a substitute for professional medical advice. If you or someone you know is in distress, please seek help from a qualified professional.
