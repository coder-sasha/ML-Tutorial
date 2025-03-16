"""
This example demonstrates the use of NLP for text summarization.
Summarization is a technic of reducing a long text to few sentences without losing the meaning.

NLTK is the out of box tool for the effective summarization.
In this script we calculate a semantic weight or a score of each sentence in the text.
We do it by assigning a score to each word in the sentence based on its frequency and position in the text, 
and then summing the scores of all the words in the sentence.
To summarize we select the top n sentences with the highest scores by sorting the sentence scores in descending order.

Mind that results much depend on how meaningful is the original text...
"""

import nltk
from nltk.corpus import stopwords
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import re

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


texts = ["- Minimum 5 years of hands-on Software Development experience in C++.\n \
- Experience working in fixed income transaction processing with good knowledge of fixed income products.\n \
- Good understanding on OOP fundamentals, Data structures, Design patterns, STL templates.\n \
- Good knowledge and experience with message based systems (Tibco RV/IBM MQ/Zero MQ).\n \
- Strong SQL and related DB skills – indexing, transaction management (Sybase/Oracle/MS SQL).\n\
- Good working knowledge of software configuration management systems - bug tracking, source control, build management (JIRA/SVN/Git/Cruise Control).\n \
- Hands on experience in scripting languages like Python/Perl.\n \
- Good experience with Windows environment.\n \
- Good problem solving and analytical skills.\n \
- Good communication skills.\n \
- Prior Repo/Sec Lending/Collateral management experience is a major plus.\n \
- FIS/Sungard Martini/APEX and/or other Repo trading platform experience is a major plus.\n \
- Experience working with front-office users/traders is a major plus.\n \
Primary / Secondary / Tertiary Skills : C++ / SQL / Python.\n",

"The Portugal football captain has made history by becoming the all-time top scorer in men's international football.\n \
The captain scored his 110th and 111th goals in his side's 2-1 World Cup qualifying win over the Republic of Ireland.\n \
Christian Ronaldo, who is 36, surpassed the previous record held by Iran's Ali Daei, who scored 109 international goals between 1993 and 2006.\n \
\"From an individual point of view, I'm proud,\" Ronaldo said after the match.\n \"From a collective point of view, it's a great victory.\"",

"Right now, you can get Chart School Live, IBD’s master class in technical analysis, for $750 when you sign up before President’s Day with a 25% discount from the regular price.\n \
This course is a must-watch for any investor.\n \
Whether you are new to reading stock charts or have some experience, you’ll come away with a deeper understanding of how to use charts to guide your buying and selling decisions.\n \
Chart School Live features four sessions on analyzing stock charts, identifying stocks ready to break out \
and adding to your positions at optimal times.\n \
In addition, you’ll learn essential selling rules for maximizing gains and protecting capital in all market conditions.\n \
Plus, you’ll have access to the recording for three years after purchase so you can refresh your skills anytime."]


for text in texts:
    # remove stop words and punctuations
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

    clean_text = text
    sentences = sent_tokenize(clean_text)

    # calculate sentence scores
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in words:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = 0
                    
                sentence_scores[sentence] += 1/len(sentences)

    # select top sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]
    summary = ' '.join(summary_sentences) 

    # print results
    print(f"Original Text (the length: {len(text)})\n--------------------------\n{text}\n")
    print(f"The NLTK Summary:\n{summary}\nthe summary length: {len(summary)}\n")

    # create a parser and tokenize the text
    summy_parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # summarize, using the LexRank summarizer
    summarizer = LexRankSummarizer()
    smr = summarizer(summy_parser.document, sentences_count=3)

    # the sumy's results ia  alist of object Sentence
    summary = ''
    for sent in smr:
        summary = f"{summary}{sent}\n"
    print(f"The Sumy Summary:\n{summary}the summary length: {len(summary)}\n")
