import google.generativeai as genai
import streamlit as st

# Configure the Google Generative AI API key
GOOGLE_API_KEY = "AIzaSyBbGoKXIEDgSoqmfLSYDgmsxpq9FyAe4m8"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the generative model (assuming correct usage)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_chatbot_response(user_input):
    # Generate content using the model
    response = model.generate_content(user_input)
    return response.text  
# Assuming .text gives the response string

# Streamlit interface setup
st.set_page_config(page_title="Simple Chatbot", layout="centered")
st.title("👨🏻‍🚀 Simple Chatbot 👨🏻‍🚀")
st.write("Powered by Google Generative AI")

# Initialize chat history in session state
if "history" not in st.session_state:
    st.session_state["history"] = []

with st.form(key="Chat_form",clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")

# Handling form submission
if submit_button:
    if user_input:
        # Get response from the chatbot
        response = get_chatbot_response(user_input)
        # Store user input and response in session history
        st.session_state.history.append({"user": user_input, "bot": response})
    else:
        st.warning("Please enter a prompt")

# Display chat history
for chat in st.session_state.history:
    st.write(f"**You:** {chat['user']}")
    st.write(f"**Bot:** {chat['bot']}")
