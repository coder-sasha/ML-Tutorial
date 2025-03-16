"""
NLP Sentiment Analysis allows us to use computers to get an insight into public opinion.
It helps to find and quantify emotions in the text data, in other words define "sentiments of a text".

The example demonstrates usage out of box NLP tools for sentiment analysis.
NLTK VADER and TextBlob are popular NLP packages that are used for sentiment analysis.
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

from textblob import TextBlob

texts = ["This movie is just great! I loved it!", "It was a boring nonsense", "I do not know, the movie seems not bad"]

# sentiment analysis using NLTK
for text in texts:
    print(f"The text: '{text}'\n---------")

    print('Analysing with NLTK')
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    print(f"\tNLTK SentimentIntensityAnalyzer Score:\t {scores['compound']:.2f}")

    # sentiment analysis using VADER	
    analyzer = SentimentIntensityAnalyzer()

    vader_scores = analyzer.polarity_scores(text)
    vscore = vader_scores['compound']
    analysis_result = f"VADER score: {vscore}"
    if vscore > 0:
        analysis_result = f"Positive sentiment,{analysis_result}"
    elif vscore < 0:
        analysis_result = f"Negative sentiment,{analysis_result}"
    else:
        analysis_result = f"Neutral sentiment,{analysis_result}"
    print(f"\t{analysis_result}")

    # sentiment analysis using TextBlob
    print('Analysing with TextBlob')
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    analysis_result = f"\t  {sentiment:.2f} {subjectivity:.2f}"

    if sentiment > 0.4 and subjectivity > 0.5:
        analysis_result = f"Strongly positive and subjective sentiment:{analysis_result}"
    elif sentiment > 0 and subjectivity <= 0.5:
        analysis_result = f"Positive and objective sentiment:{analysis_result}"
    elif sentiment < 0 and subjectivity > 0.5:
        analysis_result = f"Strongly negative and subjective sentiment:{analysis_result}"
    elif sentiment < -0.4 and subjectivity <= 0.5:
        analysis_result = f"Negative and objective sentiment:{analysis_result}"
    else:
        analysis_result = f"Neutral sentiment: {analysis_result}"

    print(f"\t{analysis_result}\n")
