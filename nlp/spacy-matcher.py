import spacy

nlp = spacy.load('en_core_web_md')

# Import spaCy Matcher
from spacy.matcher import Matcher

# Initialize the matcher with the spaCy vocabulary
matcher = Matcher(nlp.vocab)

doc = nlp("Smart people drink green tea at the morning")

# Define rule
pattern = [{'TEXT': 'green'}, {'TEXT': 'tea'}]

# Add rule
matcher.add('tea_rule', [pattern])

matches = matcher(doc)
print(f"matches: {matches}")

# Let’s make it usable - extract matched text
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)

t1 = 'I read this book'
t2 = 'I was going to book that room'
	
pattern = [{'TEXT': 'book', 'POS': 'NOUN'}]
matcher.add('book_rule', [pattern])

for t in [t1, t2]:
    d = nlp(t)
    m = matcher(d)
    if len(m) > 0:
        for match_id, start, end in m:
            # Get the matched span
            matched_span = d[start:end]
            print(f"the match is '{matched_span.text}' from the text '{t}'")        

doc1 = nlp(t1)
doc2 = nlp(t2)
print(f"the similarity: {doc1.similarity(doc2)}")
