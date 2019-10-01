import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

def text2entity(text):
    '''
    do named entity recognition for one thread/comment

    input
    -----
    str text: original text

    output
    -----
    list: list of entities
    '''

    doc = nlp(text)
    ents = [str(ent) for ent in doc.ents]
    return ' '.join(ents)

def ner(ds):
    '''
    wrapper for named entity recognition by spacy

    input
    -----
    pd.df ds: dataframe with text

    output
    -----
    pd.df entity: dataframe with entities generated for each entry
    '''

    entity = pd.DataFrame()

    n = ds.shape[0]
    i = 0
    for ind, val in ds['text'].items():
        i += 1
        # print out the progress in % every 1000 entries
        if i%1000 == 0:
            print(str(round(i/n*100, 2))+'%')

        # do entity recognition
        en = text2entity(val)
        if not en: # some text has no entity, skip
            continue

        entry = pd.DataFrame([[ind, en]], columns = ['index', 'entity'])
        entity = entity.append(entry)

    return entity.set_index('index')