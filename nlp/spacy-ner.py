import spacy

nlp = spacy.load('en_core_web_md')

txt = """ Apple Inc. announced on Monday that it will open a new office in San Francisco next month. 
CEO Tim Cook confirmed that the company plans to invest $2 billion in research and development. 
The announcement comes after a record-breaking quarter where Apple reported revenues of $81.43 billion, 
making it the highest earning tech company of 2023. Meanwhile, Microsoft Corporation, headquartered in Redmond, 
Washington, continues to expand its cloud services globally.
"""

doc = nlp(txt)

for ent in doc.ents:
    print(f"{ent.text:<25}{ent.label_:<25}")

print(spacy.explain('GPE'))

print(spacy.explain('CARDINAL'))