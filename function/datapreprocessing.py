from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences 
import pandas as pd
import string
import re
def ReadData(path):
    df=pd.read_csv(path,encoding='utf-8')
    return df['comment'], df['label']
def wordseparation(comment):
    return [review.split() for review in comment]
def Padding(Vi,X_train_corpus):
    vi_sequence=X_train_corpus.texts_to_sequences(Vi)
    vi_sequence=pad_sequences(vi_sequence,maxlen=131,padding='pre')
    return vi_sequence
def CreateCorpus(Vi):
    tokenizer=Tokenizer(oov_token='<oov>')
    tokenizer.fit_on_texts(Vi)
    return tokenizer
def Standardization(comment):
    if comment =='Positive':
        return "Đây là một bình luận mang ý nghĩa tích cực cho thấy khách hàng rất thích"
    elif comment =='Negative':
        return "Đây là một bình luận mang ý nghĩa tiêu cực cho thấy khách hàng không thích"
    else:
        return "Đây là một bình luận chứa ý kiến không rõ ràng"
def remove_pucntuation(comment):
  # Create a translation table
  translator = str.maketrans('', '', string.punctuation)
  # Remove punctuation
  new_string = comment.translate(translator)
  # Remove redudant space and break sign
  new_string = re.sub('[\n ]+', ' ', new_string)
  # Remove emoji icon
  emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                           "]+", flags=re.UNICODE)
  new_string = re.sub(emoji_pattern, '', new_string)

  return new_string
def read_filestopwords():
    with open('./DataPhone/vietnamese-stopwords.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        words = [line.split('\n')[0] for line in lines]
    return words
def remove_stopword(comment):
  stop_words = read_filestopwords()
  filtered = [word for word in comment.split() if word not in stop_words]
  return ' '.join(filtered)