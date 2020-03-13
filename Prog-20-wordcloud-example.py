import jieba
from scipy.misc import imread  #这是一个处理图像的函数
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

text='''
1905年，于右任、邵力子等原震旦公学学生脱离震旦，拥戴马相伯在吴淞创办复旦公学。
校名撷取自《尚书大传·虞夏传》“卿云烂兮，纠缦缦兮；日月光华，旦复旦兮”两句中的“复旦”二字，
本义是追求光明，寓含自主办学、复兴中华之意。马相伯、严复等先后担任校长。
1913年李登辉开始担任校长，一直到1936年。
在他长达23年的校长任内，复旦发展成为一所以培养商科、经济、新闻、教育、土木等应用型人才闻名的、
有特色的私立大学，形成了从中学到研究院的完整的办学体系。
'''
#统计词频的字典
wordfreq=dict()

#装载停用词
f=open("stopword.txt",encoding='UTF8')
fl=f.readlines()
stoplist=[]
for line in fl:
  stoplist.append(line.strip('\n'))
f.close()

#切分、停用词过滤、统计词频
for w in list(jieba.cut(text,cut_all=False)):
   if len(w)>1 and w not in stoplist:
     if w not in wordfreq:
        wordfreq[w] = 1
     else:
        wordfreq[w] = wordfreq[w] + 1

#指定字体和背景模式图片
font = r'C:\Windows\Fonts\simfang.ttf'
back_color = imread('2019.png')  
image_colors = ImageColorGenerator(back_color)

#构建WordCloud对象
wc=WordCloud(collocations=False, font_path=font,
             random_state=42,
             max_font_size=200,mask=back_color,
             background_color='white',
             max_words=100)

#调用方法生成词云图
wc = wc.generate_from_frequencies(wordfreq)
wc.recolor(color_func=image_colors)

# 保存图片
wc.to_file('wordcloud.png')
