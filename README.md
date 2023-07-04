# Streamlit_Covid_vaccine-tweet-analytics-app

![Alt text](/images/twitter-sentiment-analysis1.jpg)

Build a streamlit app for the classifcation of tweet using pretrained models from Huggingface. Huggingface provides access to various pre-trained models for sentiment analysis, including BERT, RoBERTa, and DistilBERT, among others.

## Summary
| Code      | Name        | Published Article |  Deployed App |
|-----------|-------------|:-------------:|------:|
| LP5 | Covid_vaccine-tweet-analytics-app with Streamlit |  [Medium Article](https://medium.com/@alidu143/building-a-streamlit-webapp-for-the-analyses-of-sentiment-towards-the-covid-vaccines-from-tweets-c5552cc88e1c) | [deployed app](https://huggingface.co/spaces/Abubakari/Covid_Vaccines_Tweet_Sentiment_Analysis) |

## Project Description
- The **Covid_vaccine-tweet-analytics-app** is a Streamlit web application that uses pre-trained models from Huggingface to classify the sentiment of tweets related to Covid-19 vaccines.

- The app allows users to enter a keyword or phrase related to Covid-19 vaccines and displays the sentiment analysis of the resulting tweets in real-time.

- The models used in the app include **BERT**, **RoBERTa**, and **DistilBERT**, which are state-of-the-art natural language processing models. 

- More details on the modelling can be found [here](https://medium.com/@alidu143/analyzing-sentiment-towards-the-covid-vaccines-using-pretrained-huggingface-models-8222d2e3610d) and [here](https://github.com/aliduabubakari/Analysing-social-media-sentiment-.git)

- The app also includes a visualization of the sentiment analysis results, allowing users to easily see the distribution of positive, negative, and neutral tweets related to Covid-19 vaccines.


## Setup

## Installation

Download or Clone the repository and navigate to the project directory using the following command:

```bash
git clone https://github.com/aliduabubakari/Streamlit-grocery-sales-prediction-app
```

Install the required packages to be able to run the evaluation locally.

You need to have `Python 3` on your system (a Python version lower than 3.10). Then you can clone this repo and being at the repo's `root :: repository_name> ...` follow the steps below:

- Windows:
```bash
  python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt
```  
Linux & MacOs: 
```bash
python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt
```

The both long command-lines have a same structure, they pipe multiple commands using the symbol `;` but you may manually execute them one after another.

1. Create the Python's virtual environment that isolates the required libraries of the project to avoid conflicts;

2. Activate the Python's virtual environment so that the Python kernel & libraries will be those of the isolated environment;

3. Upgrade Pip, the installed libraries/packages manager to have the up-to-date version that will work correctly;

4. Install the required libraries/packages listed in the requirements.txt file so that it will be allow to import them into the python's scripts and notebooks without any issue.

NB: For MacOs users, please install Xcode if you have an issue.


Alternatively, you can visit:

``` bash
https://huggingface.co/spaces/Abubakari/Sales_Prediction#sales-prediction-app

```  

## App Execution on huggingface 
Here's a step-by-step process on how to use the Streamlit_Covid_vaccine-tweet-analytics-app

Open the web app in your browser.

1. Select a model from the dropdown menu
2. Enter text in the text area
3. Click the 'Analyze' button to get the predicted sentiment of the text

![Alt text](/images/1.jpg)

![Alt text](/images/3.jpg)

![Alt text](/images/2.jpg)

![Alt text](/images/4.jpg)

![Alt text](5/images/.jpg)


## Contact
`Alidu Abubakari`

`Data Analyst`

`Azubi Africa`

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alidu-abubakari-2612bb57/) 

Read more on my medium: 
[Article](https://medium.com/ai-science/developing-a-streamlit-web-application-to-analyze-sentiment-towards-covid-vaccines-based-on-tweets-c5552cc88e1c) 




