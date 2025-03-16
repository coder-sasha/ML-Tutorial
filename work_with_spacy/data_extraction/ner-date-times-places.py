"""
This script demonstrates hwo to use Spacy to implement Named Entities Recognition (NER)
NER is the search of predefined terminology in the text
we read the file with statements about food, places and select dates, time and locations
"""
import spacy

# download spacy language model
nlp = spacy.load("en_core_web_md")

st_cnt = ent_cnt = 0
with open("data/statements_short.txt", "r") as statements:
    # loop through the file line by line
    for statement in statements:
        st_cnt += 1
        statement = statement.strip()
        doc = nlp(statement)

        # check the document's entities
        ents = doc.ents
        ent_found = []
        if ents:
            for ent in ents:
                if ent.label_ == "GPE" or ent.label_ == "TIME" or ent.label_ == "DATE":
                    ent_found.append(ent.text)

        if len(ent_found) > 0:
            print(f"{statement}\n{ent_found}")
            ent_cnt += len(ent_found)
            
print(f"{ent_cnt} were found in {st_cnt} statements")            
