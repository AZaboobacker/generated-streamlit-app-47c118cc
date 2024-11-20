# Python Libraries
import openai
import streamlit as st
from PIL import Image

# Set page config
apptitle='Recipe Finder App'
st.set_page_config(page_title=apptitle,
                page_icon="🥗",
                layout='centered',
                initial_sidebar_state='auto')

# Title of the page 
st.title("Recipe Finder App")

# Taking user input
st.subheader("Enter your OpenAI API Key")
apikey = st.text_input("") # Remember to not expose API keys in real application

if apikey:
    openai.api_key = apikey

    st.subheader("What ingredients do you have?")
    ingredients = st.text_input("")

    if ingredients:
        model = "gpt-3" #compatible model 
        response = openai.ChatCompletion.create(
          model=model,
          messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"What can I cook with {ingredients}?"},
            ]
        )

        message_content = response.choices[0].message.content.strip()

        st.subheader(message_content)
else:
    st.error("Please enter your OpenAI API Key")

# Sidebars for user assistance and settings
st.sidebar.subheader("App Settings")
help = st.sidebar.text_area('Use this box for assistance')

# Display image on sidebar
st.sidebar.image(Image.open('relevant-image.png'))  #add relevant image for your application