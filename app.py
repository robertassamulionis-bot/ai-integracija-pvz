import streamlit as st
import openai

# Streamlit app
st.title("Text Summarizer using OpenRouter")

# API key input
api_key = st.text_input("Enter your OpenRouter API key:", type="password")

if not api_key:
    st.warning("Please enter your OpenRouter API key to continue.")
    st.stop()

# Initialize OpenAI client with OpenRouter base URL
client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Text area for user input
user_text = st.text_area("Enter the text you want to summarize:", height=200)

# Slider for summary length
summary_length = st.slider("Summary length (words):", min_value=30, max_value=150, value=100)

# Button to trigger summarization
if st.button("Summarize"):
    if user_text.strip():
        # Create chat completion request
        response = client.chat.completions.create(
            model="stepfun/step-3.5-flash:free",
            messages=[
                {"role": "user", "content": f"Please summarize the following text in approximately {summary_length} words:\n\n{user_text}"}
            ]
        )
        # Extract and display the summary
        summary = response.choices[0].message.content
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")