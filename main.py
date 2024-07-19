import spacy

# import the spacy model, which is usually a folder in this directory
# for example, a folder in the same directory called `trained_model`
# would be imported like so:
nlp = spacy.load("trained_model")

# define the text you would like to use the trained model to predict on
text = """The unemployment rates in the United States have ranged beween 3% and
12%, depending on the category. Jerome Powell said in a speech on Friday that
the Fed will do everything it can to control and contain inflation. Their
target is at 2% per year.
"""

# run the text through the spacy object
doc = nlp(text)

# find all the predicted entities in this text and iterate over them
for ent in doc.ents:
    # package key information into a dictionary for easy reference
    d = {
        'ner_predicted': ent,
        'ner_label': ent.label_
    }
    # print them out for viewing
    print(d)

# example print out:
# {'ner_predicted': the United States, 'ner_label': 'GPE'}
# {'ner_predicted': 3%, 'ner_label': 'PERCENT'}
# {'ner_predicted': 12%, 'ner_label': 'PERCENT'}
# {'ner_predicted': Jerome Powell, 'ner_label': 'PERSON'}
# {'ner_predicted': Friday, 'ner_label': 'DATE'}
# {'ner_predicted': Fed, 'ner_label': 'ORG'}
# {'ner_predicted': 2%, 'ner_label': 'PERCENT'}

# in this case, the trained_model was based off of en_core_web_trf 
# reference: https://spacy.io/models/en#en_core_web_trf
# NER label scheme: CARDINAL, DATE, EVENT, FAC, GPE, LANGUAGE, LAW, LOC, MONEY, NORP, ORDINAL, ORG, PERCENT, PERSON, PRODUCT, QUANTITY, TIME, WORK_OF_ART

