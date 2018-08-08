#获取个人微信号中朋友信息
#导入itchat包
import itchat
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS


#获取个人微信号好友信息
if __name__=="__main__":
    #登录个人微信，扫码登录
    itchat.login()
    #爬取自己好友相关信息
    friends=itchat.get_friends(update=False)[0:]
    # define a list for store the signature of my friends 
    list = []

    for user in friends:
        str = user.get('Signature')
        list.append(str)

    background = plt.imread('book.jpg')
    wc = WordCloud(background_color = 'white',
        mask = background,
        max_words = 2000, #设置最大现实字数
        stopwords = STOPWORDS, #设置停用词
        font_path = '',
        max_font_size = 50, #设置字体最大值
        random_state = 30, #配色方案种数)

