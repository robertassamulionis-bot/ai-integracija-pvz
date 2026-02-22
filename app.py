import streamlit as st
import openai

# Read API key from file
with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

# Initialize OpenAI client with OpenRouter base URL
client = openai.OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Streamlit app
st.title("Text Summarizer using OpenRouter")

# Text area for user input
user_text = st.text_area("Enter the text you want to summarize:", height=200)

# Button to trigger summarization
if st.button("Summarize"):
    if user_text.strip():
        # Create chat completion request
        response = client.chat.completions.create(
            model="stepfun/step-3.5-flash:free",
            messages=[
                {"role": "user", "content": f"Please summarize the following text:\n\n{user_text}"}
            ]
        )
        # Extract and display the summary
        summary = response.choices[0].message.content
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")