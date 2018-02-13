import urllib.request
from bs4 import BeautifulSoup

def getHtml(url , headers):
    req = urllib.request.Request(url = url , headers = headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    return html

def saveTxt(path , html):
    f = open(path , "wb")
    f.write(html)

def praseHtml(currentURL , headers, path):

    #html = html.decode('utf-8')
    chapter = 153
    flag = 1
    while flag:
        chapter = chapter + 1
        if chapter >= 257:
            flag = 0
        # 因为章节太多了，所以就手动控制只爬取了前20章
        html = getHtml(currentURL , headers)
        savePath =path +\
        str(chapter) + ".txt"
        # 将多章节分开存放，每一章节存为一个单独的txt文件，文件与章节书想对应，例如第一章就存为 1.txt
        f = open(savePath , "w")
        soup =  BeautifulSoup(html,'lxml')
        nameText = soup.find('h1',attrs={'class':'nr_title'})
        contentText = soup.find('div',attrs = {'id':'nr1'})
        result = nameText.getText() + '\n' + contentText.getText()
        result = result.replace('　　','\n  ')
        f.write(result)
        #到此实现第一章的爬取
        nextpage = soup.find('a' ,attrs = {'id':'pb_next'})
        if nextpage :
            currentURL = nextpage['href']
        else :
            currentURL = None
            flag = 0



def main():
    url="https://m.yushuwu.org/novel/57176/7400248.html"
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    path = "/Users/Alice/Desktop/3/"
# "###"代表的是相应的存放位置，然后将相应的多个文本文件存放在novel文件夹中
    praseHtml(url , headers , path)
    #saveTxt(path , html)

main()