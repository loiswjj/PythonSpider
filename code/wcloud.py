#encoding=utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import jieba
import numpy as np
import os
from PIL import Image
import xlwt,xlrd

def getfileStr(path):
	# get all files under path
	files = os.listdir(path)
	str = ""
	for file in files:
		if not os.path.isdir(file):
			f = open(path+"/"+file)
			iter_f = iter(f)
			filestr = ""
			for line in iter_f:
				filestr = filestr + line
				filestr = filestr.strip()
			str += filestr
	return str

str = getfileStr("songlist")

#词云
'''str = str.replace("作曲","")
str = str.replace("作词","")
str = str.replace("编曲","")
wordlist = jieba.cut(str)
splitlist = "".join(wordlist)

coloring = np.array(Image.open("pic.jpg"))
my_wordcloud = WordCloud(font_path="H-XiuYue-CuTi/H-SiuNiu-Bold-2.ttf",background_color="white",mask=coloring,
                max_font_size=50, random_state=42).generate(splitlist)

image_color = ImageColorGenerator(coloring)

plt.imshow(my_wordcloud,interpolation="bilinear")
plt.axis("off")
plt.show()'''

#歌词词频统计
wordlist = jieba.cut(str)

word_list = []
word_dict = {}
for item in wordlist:
	if len(item)>1:
		word_list.append(item)

for key in word_list:
	if key in word_dict:
		word_dict[key] += 1
	else:
		word_dict[key] = 1

sorted(word_dict.items(),key=lambda item:item[1],reverse=False)

'''fc = open("split.txt",'w')
for item in word_dict.items():
	fc.write(item[0]+str(item[1])+'\n')'''

file = xlwt.Workbook()
table = file.add_sheet('My Worksheet')

index = 0

for item in word_dict:
	table.write(index,0,item)
	table.write(index,1,word_dict[item])
	index +=1

file.save("split.xls")