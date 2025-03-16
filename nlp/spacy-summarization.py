"""
The second summarization example
We use spacy and graph representation of a text
"""

import spacy
import networkx as nx
import numpy as np

nlp = spacy.load("en_core_web_md")

texts = ["Cristiano Ronaldo has made history by becoming the all-time top scorer in men's international football.\n \
The Portugal captain scored his 110th and 111th goals in his side's 2-1 World Cup qualifying win over the Republic of Ireland.\n \
Ronaldo, 36, surpassed the previous record held by Iran's Ali Daei, who scored 109 international goals between 1993 and 2006.\n \
\"From an individual point of view, I'm proud,\" Ronaldo said after the match.\n \"From a collective point of view, it's a great victory.\"",
"- Minimum 5 years of hands-on Software Development experience in C++.\n \
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
"Right now, you can get Chart School Live, IBD’s master class in technical analysis, for $750 when you sign up before President’s Day with a 25% discount from the regular price.\n \
This course is a must-watch for any investor.\n \
Whether you are new to reading stock charts or have some experience, you’ll come away with a deeper understanding of how to use charts to guide your buying and selling decisions.\n \
Chart School Live features four sessions on analyzing stock charts, identifying stocks ready to break out \
and adding to your positions at optimal times.\n \
In addition, you’ll learn essential selling rules for maximizing gains and protecting capital in all market conditions.\n \
Plus, you’ll have access to the recording for three years after purchase so you can refresh your skills anytime."]

for text in texts:
    # as always we process the text through spacy pipe
    doc = nlp(text)

    # split the text into individual sentences
    sentences = [sent.text.strip() for sent in doc.sents]

    # create a list of stopwords
    stopwords = list(nlp.Defaults.stop_words)

    # remove stopwords and punctuation, and lemmatize the remaining words
    lemmatized_sentences = []
    for sentence in sentences:
        words = []
        for word in nlp(sentence):
            if not word.is_stop and not word.is_punct:
                words.append(word.lemma_)
                
        lemmatized_sentences.append(" ".join(words))

    # calculate the similarity matrix
    sim_matrix = []
    for i in range(len(lemmatized_sentences)):
        row = []
        for j in range(len(lemmatized_sentences)):
            row.append(nlp(lemmatized_sentences[i]).similarity(nlp(lemmatized_sentences[j])))

        sim_matrix.append(row)

    # convert the similarity matrix to a graph
    graph = nx.from_numpy_array(np.array(sim_matrix))

    # calculate the PageRank scores
    scores = nx.pagerank(graph)

    # Sort the sentences by their scores and extract the top n sentences (2 as in nltk-summarization)
    num_sentences = 2
    top_sentence_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:num_sentences]
    summary = [sentences[i] for i in top_sentence_indices]
    smr = " ".join(summary)

    # Print the summary
    print(f"Original Text (the length: {len(text)})\n--------------------------\n{text}\n")
    print(f"and the Summary:\n{smr}\nthe summary length: {len(smr)}")
    print()
