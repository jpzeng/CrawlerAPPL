# -*- coding: utf-8 -*-
import jieba
import os
import chardet
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel
from wordcloud import WordCloud
import matplotlib.pyplot as plt


num_topics=5
newsTextdir = r'.\news'

def getnewstext(newsdir):
  docs=[]
  news_text=""
  sd=os.walk(newsdir)
  for d,s,fns in sd:
     for fn in fns:
          if fn[-3:]=='txt':
               file=d+os.sep+fn
               print(file)
               try:
                  f=open(file)
                  lines=f.readlines()
               except:
                  ft=open(file,"rb")
                  cs=chardet.detect(ft.read())
                  ft.close()
                  f=open(file,encoding=cs['encoding'])
                  lines=f.readlines()
               docs.append('\n'.join(lines))
  return docs

alllines=getnewstext(newsTextdir)

#对文档集进行词汇切分、停用词过滤
stoplist=open('stopword.txt','r',encoding="utf-8").readlines()
stoplist = set(w.strip() for w in stoplist)

segtexts=[]
for line in alllines:
    doc=[]
    for w in list(jieba.cut(line,cut_all=True)):
        if len(w)>1 and w not in stoplist:
            doc.append(w)
    segtexts.append(doc)

dictionary = Dictionary(segtexts)
dictionary.filter_extremes(2,1.0,keep_n=1000) #词典过滤，保留1000个
corpus = [dictionary.doc2bow(text) for text in segtexts]
lda = LdaModel(corpus,id2word=dictionary, num_topics=num_topics) #指定id2word，可以直接显示词汇而非其id
topics=lda.print_topics(num_topics=num_topics,num_words=10) #list (topic_id, [(word, value), … ])
print(topics)
#可视化
font = r'C:\Windows\Fonts\simfang.ttf'
wc=WordCloud(collocations=False, font_path=font, width=2800, height=2800, max_words=20,margin=2)
for topicid in range(0,num_topics):
    tlist=lda.get_topic_terms(topicid, topn=1000)   #定义词云图中的词汇数  p(w|z)
    #print(tlist)
    wdict={}   #['词a':100 '词b':90,'词c':80]
    for wv in tlist:
        wdict[ dictionary[wv[0]]]=wv[1]
    print(wdict)
    wordcloud = wc.generate_from_frequencies(wdict)
    wordcloud.to_file('topic_'+str(topicid)+'.png')  #保存图片
