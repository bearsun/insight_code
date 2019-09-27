import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

def text2entity(text):
    doc = nlp(text)
    ents = [str(ent) for ent in doc.ents]
    return ' '.join(ents)

ds = pd.read_csv('ds.csv', index_col=0, nrows = 539272)
ds.dropna(inplace = True)

entity = pd.DataFrame()

n = ds.shape[0]
i = 0
for ind, val in ds['text'].items():
    i += 1
    if i%1000 == 0:
        print(str(round(i/n*100, 2))+'%')
    en = text2entity(val)
    if not en:
        continue
    entry = pd.DataFrame([[ind, en]], columns = ['index', 'entity'])
    entity = entity.append(entry)

entity.set_index('index').to_csv('entity1.csv')