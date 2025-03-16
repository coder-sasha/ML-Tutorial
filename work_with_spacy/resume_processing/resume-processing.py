"""
This script demonstrates how to use NLP and spaCy for resume analysis.
We use a dataset of resume consumed by pandas DataFrame and spaCy to extract form resume relevant terminology and
define what resumes are semantically close to the fob description.

spaCy’s is trained for general purpose datasets.
For specific domains off-the-shelf models might fail because they have not been trained on domain-specific texts.
To solve this problem we can use a special spaCy’s feature - entity ruler.
The Entity Ruler enables us to create a set of patterns with corresponding labels, and then use it to find and
label entities in domain-specific texts.
For extracting IT skills, we use a prepared skill dataset - a jsonl file which contains label and patterns,
used to describe skills in various resume.

We extract IT skills from the job description and compare them with skills extracted from resumes to identify the best match.
We also will do some visualization exercise to illustrate our results.
"""

# spacy
import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English
from spacy.tokens import Doc

# Visualization
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Data loading/ Data manipulation
import pandas as pd
import numpy as np

# regular expressions
import re

# warning
import warnings
warnings.filterwarnings('ignore')

# the list os spaCy stopwords: a, an, the etc. 
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
nlp = spacy.load('en_core_web_md')

# add IT skills to spaCy language model
skills_path = "data\\skills_patterns.jsonl"
ruler = nlp.add_pipe('entity_ruler')
ruler.from_disk(skills_path)
# uncomment if you want to see names of spaCy pipe calls
# print(nlp.pipe_names)

# utils
def prepare_job_doc(jb_path: str) -> object:
    """ read text from given file and return spaCy doc object """
    with open(jb_path, 'r') as job_file:
        job = job_file.read()

    jclean = clean_text(job)
    jskills = unique_skills(get_skills(jclean))
    jwords = " ".join(jskills)

    jdoc = nlp(jclean)

    return jdoc


def get_skills(text: str) -> list:
    """ using spaCy NER and skill_patterns build and return a list of IT skills """    
    doc = nlp(text)
    subset = []
    for ent in doc.ents:
        if ent.label_ == 'SKILL':
            subset.append(ent.text)

    return subset


def unique_skills(sklls: list) -> list:
    """ remove duplicate skills """    
    return list(set(sklls))


def clean_text(in_text: str) -> str:
    """ remove stop words, punctuation and special terms from a text """
    txt = re.sub(r'[^a-zA-Z0-9\s]', "", in_text)
    doc = nlp(txt)
    cln_text = [token.lemma_.lower() for token in doc if str(token).strip()
                and not token.is_stop
                and not token.is_punct
                and not token.like_url
                and not token.like_email
                ]

    return " ".join(cln_text)

# processing
df = pd.read_csv("data\\it_resumes_str.csv")
selected_cols = ['ID', 'Resume_str', 'Category']
df_selected = df[selected_cols]
print(f"downloaded {len(df)} resumes")
print(df_selected.head(5))
print(df_selected.tail(3))

# clean text: remove stopwords, punctuation, emails and urls
data = pd.DataFrame(df['ID'])
data['Clean Resume'] = df['Resume_str'].apply(clean_text)
data['Skills'] = data['Clean Resume'].apply(get_skills)
data['Skills'] = data['Skills'].apply(unique_skills)

# see the WordCloiud picture showing skills listed in resumes
words = ''
for v in data['Skills'].values:
    words = f"{words} {v} "
    
wordcloud = WordCloud().generate(words)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Most Used Skills")
plt.show()

# read job description and process it with spaCy
jdoc = prepare_job_doc('data\\job_description.txt')

data['Job Sim'] = data['Clean Resume'].apply(lambda r: jdoc.similarity(nlp(r)))
data = data.sort_values(by='Job Sim', ascending=False)

# see the 5 resumes with the highest similarity score
print("\n5 Resumes Most Similar to the Job Description")
selected_cols = ['ID', 'Job Sim', 'Clean Resume']
df_selected = data[selected_cols]
print(df_selected.head(5))


