import spacy

nlp = spacy.load('en_core_web_md')


# extract the direct object and its transitive verb
def get_obj_verb(doc):
    it_obj = ''
    it_verb = ''
    for token in doc:
        if token.dep_ == 'dobj':
            return token, token.head
        #            it_obj = token


#            it_verb = token.head

#    return it_obj, it_verb


# extract the verb for the intent's definition
def get_intent(itobj, itverb):
    intentVerb = ''
    verbList = ['want', 'like', 'need', 'order', 'book']
    if itverb.text in verbList:
        intentVerb = itverb
    else:
        if itverb.head.dep_ == 'ROOT':
            intentVerb = itverb.head

    # extract the object for the intent's definition
    intentObj = ''
    objList = ['pizza', 'cola', 'soda', 'beer', 'burritos']
    if itobj.text in objList:
        intentObj = itobj
    else:
        for child in itobj.children:
            if child.dep_ == 'prep':
                intentObj = list(child.children)[0]
                break
            elif child.dep_ == 'compound':
                intentObj = child
                break

    return intentVerb, intentObj


texts = ['I want to place an order for a big Sicilian pizza with some light beer.',
         'I order a pizza launch with soda.',
         'They make excellent burritos and pizzas.']

for txt in texts:
    doc = nlp(txt)
    obj, verb = get_obj_verb(doc)
    intent_verb, intent_obj = get_intent(obj, verb)
    # print the intent expressed in the sample sentence
    print(f"the intent in the '{txt}' is: '{intent_verb.text}  {intent_obj.text}'")
