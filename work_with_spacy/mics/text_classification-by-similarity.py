"""
The text similarity plays a key role in NLP
It is used for information retrieval, recommendation systems, and document clustering. 
Spacy provides powerful tools for measuring text similarity. 
This script demonstrates how Spacy’s similarity functionality can be used to solve some NLP problems.
"""

import spacy

nlp = spacy.load("en_core_web_md")

sent1 = 'I love pizza'
sent2 = 'I adore oatmeal'

doc1 = nlp(sent1)
doc2 = nlp(sent2)

similarity = doc1.similarity(doc2)
print(f"Similarity score between '{sent1}' and '{sent2}' is {similarity}\n")

phrases = {'during my trip service was excellent': [],
           'this food is terrible': [],
           'the show was great': [],
           'all those books are just terrible junk': [],
           'her journey was acceptable': [],
           }

print('Phrase to Phrase Comparison')
results = {}
for p_phrase in phrases:
    p_doc = nlp(p_phrase)
    vsim = 0
    results[p_phrase] = ['', 0]
    for phrase in phrases:
        m_doc = nlp(phrase)
        sim = p_doc.similarity(m_doc)
        phrases[phrase].append(sim)
        if sim > vsim and phrase != p_phrase:
            results[p_phrase] = phrase, sim
            vsim = sim

    print(f"'{p_phrase}' is most similar to '{results[p_phrase][0]}', the similarity is {results[p_phrase][1]}")
