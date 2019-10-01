import string
import re

def preprocess_one(text, b_punct):
	'''
	basic preprocessing of the text, including:
	1) remove links and emojis
	2) remove special char like 🏀
	3) remove \n \t \r

	input
	-----
	str text: a single thread/comment
	bool b_punct: boolean to indicate whether to remove punctuation

	output
	-----
	str cleaned3: cleaned text
	'''

    # remove links and emojis
    cleaned1 = re.sub(r'((http|ftp|https):\/\/)?[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?', ' ', str(text))

    #replace special char like 🏀
    cleaned2 = cleaned1.encode('ascii', 'ignore').decode('ascii')
    
    #remove \n \t \r
    cleaned3 = cleaned2.translate(str.maketrans("\n\t\r", "   "))
    
    if b_punct:
        #replace punctuation with space
        cleaned3 = ''.join([c if c not in string.punctuation else ' ' for c in cleaned3])
    
    return cleaned3
