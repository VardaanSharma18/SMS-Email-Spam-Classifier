import nltk
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_message(mssg):
    mssg = mssg.lower()
    mssg = nltk.word_tokenize(mssg)

    text = []
    for i in mssg:
        if i.isalnum():
            text.append(i)
    mssg = text.copy()
    text.clear()

    for i in mssg:
        if i not in stopwords.words('english') and i not in string.punctuation:
            text.append(i)
    mssg = text.copy()
    text.clear()

    for i in mssg:
        text.append(ps.stem(i))

    return " ".join(text)
