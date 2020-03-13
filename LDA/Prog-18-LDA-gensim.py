# -*- coding: utf-8 -*-
import jieba, os
import codecs
from gensim import corpora, models, similarities
 
def load_data():
    documents = []
    raw = codecs.open('world-cup.raw', 'r', 'utf-8','ignore').readlines()
    for doc in raw:
       documents.append(doc)
    return documents
 
def preprocess(documents):
    stoplist = codecs.open('stopword.txt','r',encoding='utf8').readlines()
    stoplist = set(w.strip() for w in stoplist)
    #分词，去停用词
    texts=[]
    for document in documents:
        doc=[]
        for word in list(jieba.cut(document,cut_all=True)):
          if len(word)>=2:
             if word not in stoplist:
                 doc.append(word)
        texts.append(doc)
    
    dictionary = corpora.Dictionary(texts)
    dictionary.filter_extremes(no_below=3, no_above=1.0,keep_n=1000)
    
    dictionary.save('LDA.dict')
    corpus = [dictionary.doc2bow(text) for text in texts]
    return corpus,dictionary

def train():
    documents = load_data()
    corpus,dictionary = preprocess(documents)
    lda = models.LdaModel(corpus, id2word = dictionary, num_topics = 2)
    #模型的保存/ 加载
    lda.save('LDA.model')
        
def test(test_doc):
    lda = models.ldamodel.LdaModel.load('LDA.model')     
    dictionary = corpora.Dictionary.load('LDA.dict')
    test_doc = list(jieba.cut(test_doc)) # 新文档进行分词
    docs=[]
    docs.append(test_doc)

    corpus = [dictionary.doc2bow(text) for text in docs]
 
    p=lda.log_perplexity(corpus)
    return p


if __name__ == '__main__':
    train()
    print('困惑度=',test( '2018世界杯足球赛的直播平台开始试运营了')) 
    print('困惑度=',test( '大数据技术给各个行业运营注入了新的希望'))

 

