from gensim.summarization import keywords

f = open('txt_corpus.txt', 'r')
corpus = f.read()
f.close()

kwords = keywords(corpus, words = 3000, split=True)

f = open('txt_kwords.txt', 'w')
f.write('@'.join(kwords))
f.close()
