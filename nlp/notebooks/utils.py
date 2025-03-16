# for numerical analysis
import numpy as np
# to store and process in a dataframe
import pandas as pd

# for plotting graphs
import matplotlib.pyplot as plt

# advance plotting
import seaborn as sns

# to create word clouds
from wordcloud import WordCloud, STOPWORDS
from sklearn.metrics import confusion_matrix

# text processing
import re
import nltk
from nltk.corpus import stopwords


# to plot n-gram
def category_ngram(category, n):
    temp_df = df[df['category'] == category]

    word_vectorizer = CountVectorizer(ngram_range=(n, n), analyzer='word')
    sparse_matrix = word_vectorizer.fit_transform(temp_df['headline'])

    frequencies = sum(sparse_matrix).toarray()[0]

    return pd.DataFrame(frequencies, index=word_vectorizer.get_feature_names(), columns=['frequency']) \
        .sort_values(by='frequency', ascending=False) \
        .reset_index() \
        .head(10)


# to plot wordcloud
# =================

def plot_wordcloud(headlines, cmap=None):
    fig, ax = plt.subplots(figsize=(8, 6))
    wc = WordCloud(max_words=1000, background_color='white', stopwords=stopwords,
                   min_font_size=10)  # , colormap=cmap)
    wc = wc.generate(' '.join(headlines))
    plt.axis('off')
    plt.imshow(wc)


# to plot model accuracy and loss
# ===============================
def plot_history(history):
    plt.figure(figsize=(20, 5))

    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy', c='dodgerblue', lw='2')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy', c='orange', lw='2')
    plt.title('Accuracy', loc='left', fontsize=16)
    plt.xlabel("Epochs")
    plt.ylabel('Accuracy')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss', c='dodgerblue', lw='2')
    plt.plot(history.history['val_loss'], label='Validation Loss', c='orange', lw='2')
    plt.title('Loss', loc='left', fontsize=16)
    plt.xlabel("Epochs")
    plt.ylabel('Loss')
    plt.legend()

    plt.show()


# to plot confusion matrix
# ========================
def plot_cm(pred, ticklabels, figsize):
    fig, ax = plt.subplots(1, 1, figsize=(figsize, figsize))

    cm = confusion_matrix(validation_labels, pred)
    sns.heatmap(cm, annot=True, cbar=False, fmt='1d', cmap='Blues', ax=ax)

    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_xticklabels(ticklabels, rotation=90)
    ax.set_yticklabels(ticklabels, rotation=0)

    plt.show()


def plot_hist_categories(count_df):
    sns.set_style('darkgrid')
    plt.figure(figsize=(24, 12))
    sns.barplot(data=count_df, y='count', x='category', palette='Dark2')
    plt.title('Number of News in Each Category', loc='left', fontsize=20)
    plt.xlabel("Categories", fontsize=14)
    plt.ylabel("Numbers", fontsize=14)

    plt.show()


# removing non-alphanumeric character
def alpha_num(text):
    return re.sub(r'[^A-Za-z0-9 ]', '', text)


# removing the stopwords from text
def remove_stopwords(text):
    final_text = []
    for i in text.split():
        if i.strip().lower() not in stopwords:
            final_text.append(i.strip())

    return " ".join(final_text)
