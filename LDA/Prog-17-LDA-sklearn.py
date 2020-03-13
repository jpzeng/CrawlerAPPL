# -*- coding: utf-8 -*-

import jieba
import codecs
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def load_data():
    documents = []
    raw = codecs.open('world-cup.raw', 'r', 'utf-8','ignore').readlines()
    for doc in raw:
       documents.append(doc)
    return documents

 
def train(documents):
    stoplist = codecs.open('stopword.txt','r',encoding='utf8').readlines()
    stoplist = set(w.strip() for w in stoplist)

    #分词，去停用词
    texts=[]
    for document in documents:
        doc=''
        for word in list(jieba.cut(document,cut_all=True)):
          if len(word)>=2:
             if word not in stoplist:
                 doc=doc+' '+word
        texts.append(doc)

    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2)
    tf = tf_vectorizer.fit_transform(texts)
    dictionary=tf_vectorizer.get_feature_names()
    lda = LatentDirichletAllocation(n_components=2, 
                                learning_offset=50.,
                                random_state=0)
    lda = lda.fit(tf)
    return lda,dictionary
 
def test(lda,dictionary, test_doc):
    # 新文档进行分词
    doc_cut=jieba.cut(test_doc,cut_all=True)
    docc=[]
    for w in list(doc_cut):
        docc.append(w)
        
    doc=[]
    for w in dictionary:
        n=0
        for w2 in docc:
            if w==w2:
                n=n+1
        doc.append(n)
            
    docs=[]
    docs.append(doc)
    s=lda.perplexity(docs)
    return s 
    
if __name__ == '__main__':
    documents=load_data()
    lda,dictionary=train(documents)
    print('困惑度=',test(lda,dictionary, '2018世界杯足球赛的直播平台开始试运营了')) 
    print('困惑度=',test(lda,dictionary, '大数据技术给各个行业运营注入了新的希望'))
    

