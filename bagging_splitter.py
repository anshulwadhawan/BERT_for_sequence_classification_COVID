
labels=[]
texts=[]
ids=[]
#train_ids=[]
alphas=[]
count=0

with open('data/train.tsv','r', encoding = 'utf-8') as reader:
    for line in reader:
        line_splitted = line.split('\t')
        labels.append(line_splitted[2])
        texts.append(line_splitted[1])
        alphas.append('a')
        ids.append(count)
        #train_ids.append(line_splitted[0])
        count=count+1
        
test_ids=[]
test_texts=[]
count=0
with open('data/unlabeled_test_with_noise.tsv','r', encoding = 'utf-8') as reader:
    for line in reader:
        line_splitted = line.split('\t')
        test_texts.append(line_splitted[1])
        #alphas.append('a')
        #test_ids.append(line_splitted[0])
        test_ids.append(count)
        count=count+1

print(set(train_ids).intersection(test_ids))
print(len(test_texts))
print(len(test_ids))

binary_labels = []

for label in labels:
    if label=='INFORMATIVE\n':
        binary_labels.append('1')
    else:
        binary_labels.append('0')

print(len(binary_labels))
print(len(texts))
print(len(ids))
print(len(alphas))

labels=labels[1:]
alphas=alphas[1:]
texts=texts[1:]
ids=ids[1:]
binary_labels=binary_labels[1:]


processed_texts=[]

import re
from bs4 import BeautifulSoup

def cleanhtml(raw_html):
  #print(raw_html)
  cleantext = BeautifulSoup(raw_html).get_text()
  cleantext = re.sub(r'[^\x00-\x7f]', '', cleantext) 
  cleantext = cleantext.replace("\n","")
  cleantext = cleantext.replace("\t","")
  cleantext = cleantext.replace("HTTPURL","")
  cleantext = cleantext.replace("@USER"," ")

  return cleantext

for text in test_texts:
    processed_texts.append(cleanhtml(text).strip())

print(binary_labels[:5])
print(processed_texts[:5])
print(ids[:5])
print(alphas[:5])

print(len(max(processed_texts)))

fake_labels=['1']*len(processed_texts)
alphas=['a']*len(processed_texts)

print(len(alphas))

import pandas as pd
test_df = pd.DataFrame({
    'id': test_ids,
    'label':fake_labels,
    'alpha':alphas,
    'text': processed_texts
})


#valid_df.head()

test_df.to_csv('test_set.tsv', sep='\t', index=False, header=False, columns=test_df.columns)


train_plus_valid_df_shuffled = train_plus_valid_df_shuffled.sample(frac=1)
print(len(train_plus_valid_df_shuffled))

train_subset8_df = pd.read_csv('bagging/train_subset8.tsv',delimiter='\t',encoding='utf-8', header = None)
valid_subset8_df = pd.read_csv('bagging/valid_subset8.tsv',delimiter='\t',encoding='utf-8', header = None)


#train_df = train_plus_valid_df_shuffled.iloc[:7000, :]
#valid_df = train_plus_valid_df_shuffled.iloc[7000:, :]

print(len(train_subset8_df))
print(len(valid_subset8_df))

train_plus_valid_subset8_list = [train_subset8_df, valid_subset8_df]
train_plus_valid_subset8_df = pd.concat(train_plus_valid_subset8_list)

print(len(train_plus_valid_subset8_df))

train_plus_valid_subset8_df.columns=['id', 'label', 'alpha', 'text']
train_plus_valid_subset8_df.to_csv('bagging/train_plus_valid_subset8.tsv', sep='\t', index=False, header=False, columns=train_plus_valid_subset8_df.columns)

train_plus_valid_subset8_df.head()
train_df.to_csv('bagging/train_subset10.tsv', sep='\t', index=False, header=False, columns=train_plus_valid_df.columns)
valid_df.to_csv('bagging/valid_subset10.tsv', sep='\t', index=False, header=False, columns=train_plus_valid_df.columns)

