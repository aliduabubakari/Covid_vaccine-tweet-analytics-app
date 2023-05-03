import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from PIL import Image
import base64


# Define the "How to Use" message
how_to_use = """
**How to Use**
1. Select a model from the dropdown menu
2. Enter text in the text area
3. Click the 'Analyze' button to get the predicted sentiment of the text
"""

# Load the image
#Positive_sentiment = Image.open("Positive_sentiment.jpg")

# Load the cover image
#cover_image = Image.open('Cover_image.jpg')
#image_base64 = base64.b64encode(cover_image.getvalue()).decode('utf-8')


# Functions
def main():
    st.title("Covid Tweets Sentiment Analysis NLP App")
    st.subheader("Team Harmony Project")

    # Add the cover image
    #st.markdown(f'<img src="data:image/jpeg;base64,{image_base64}" alt="Cover Image">', unsafe_allow_html=True)

    st.image("Cover_image.jpg")

    # Define the available models
    models = {
        "ROBERTA": "Abubakari/finetuned-Sentiment-classfication-ROBERTA-model",
        "BERT": "Abubakari/finetuned-Sentiment-classfication-BERT-model",
        "DISTILBERT": "Abubakari/finetuned-Sentiment-classfication-DISTILBERT-model"
    }

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Add the "How to Use" message to the sidebar
    st.sidebar.markdown(how_to_use)

    if choice == "Home":
        st.subheader("Home")

        # Add a dropdown menu to select the model
        model_name = st.selectbox("Select a model", list(models.keys()))

        with st.form(key="nlpForm"):
            raw_text = st.text_area("Enter Text Here")
            submit_button = st.form_submit_button(label="Analyze")

        # Layout
        col1, col2 = st.columns(2)
        if submit_button:
            # Display balloons
            st.balloons()
            with col1:
                st.info("Results")
                tokenizer = AutoTokenizer.from_pretrained(models[model_name])
                model = AutoModelForSequenceClassification.from_pretrained(models[model_name])

                # Tokenize the input text
                inputs = tokenizer(raw_text, return_tensors="pt")

                # Make a forward pass through the model
                outputs = model(**inputs)

                # Get the predicted class and associated score
                predicted_class = outputs.logits.argmax().item()
                score = outputs.logits.softmax(dim=1)[0][predicted_class].item()

                # Compute the scores for all sentiments
                positive_score = outputs.logits.softmax(dim=1)[0][2].item()
                negative_score = outputs.logits.softmax(dim=1)[0][0].item()
                neutral_score = outputs.logits.softmax(dim=1)[0][1].item()

                # Compute the confidence level
                confidence_level = np.max(outputs.logits.detach().numpy())

                # Print the predicted class and associated score
                st.write(f"Predicted class: {predicted_class}, Score: {score:.3f}, Confidence Level: {confidence_level:.2f}")

                # Emoji
                if predicted_class == 2:
                    st.markdown("Sentiment: Positive :smiley:")
                    st.image("Positive_sentiment.jpg")
                elif predicted_class == 1:
                    st.markdown("Sentiment: Neutral :😐:")
                    st.image("Neutral_sentiment.jpg")
                else:
                    st.markdown("Sentiment: Negative :angry:")
                    st.image("Negative_sentiment2.png")

            # Create the results DataFrame
            # Define an empty DataFrame with columns

            results_df = pd.DataFrame(columns=["Sentiment Class", "Score"])

            # Create a DataFrame with scores for all sentiments
            all_scores_df = pd.DataFrame({
            'Sentiment Class': ['Positive', 'Negative', 'Neutral'],
            'Score': [positive_score, negative_score, neutral_score]
            })

            # Concatenate the two DataFrames

            results_df = pd.concat([results_df, all_scores_df], ignore_index=True)

            #results_df = pd.DataFrame({
            #    "Sentiment Class": [predicted_class],
            #    "Score": [score]
            #})

            # Create the Altair chart
            chart = alt.Chart(results_df).mark_bar(width=50).encode(
                x="Sentiment Class",
                y="Score",
                color="Sentiment Class"
            )

            # Display the chart
            with col2:
                st.altair_chart(chart, use_container_width=True)
                st.write(results_df)

    else:
        st.subheader("About")
        st.write("This is a sentiment analysis NLP app developed by Team Harmony for analyzing tweets related to Covid-19. It uses a pre-trained model to predict the sentiment of the input text. The app is part of a project to promote teamwork and collaboration among developers.")



if __name__ == "__main__":
    main()
