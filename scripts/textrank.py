from gensim.summarization import keywords


def textrank():
    # load the corpus
    f = open('txt_corpus.txt', 'r')
    corpus = f.read()
    f.close()

    # extract keywords
    kwords = keywords(corpus, words=3000, split=True)

    # save
    f = open('txt_kwords.txt', 'w')
    f.write('@'.join(kwords))
    f.close()
