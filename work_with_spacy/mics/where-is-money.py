"""
The script demonstrates spacy tokenization and token extraction
"""

import spacy

nlp = spacy.load('en_core_web_md')

doc = nlp("Our firm has earned this year the income of $108.5 million, \
          comparing with $101.2 million the last year \
          the growth is $7.3 million!")
money = ''

# loop through document token to find a target
for token in doc:
    if token.tag_ == '$':
        money = token.text
        x = token.i + 1
        # moving until tag is CD - 'CARDINAL NUMBER'
        while doc[x].tag_ == 'CD':
            money = f"{money}{doc[x].text} "
            x += 1

        money = money[:-1]
        print(f"money is: {money}")

