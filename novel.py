import requests
import re

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getHtmlList():
    try:
        urlList = []
        for i in range(2,3):
            url = 'http://14ckck.com/artlist/19-{}.html'.format(i)
            html = getHtmlText(url)
            pageList = re.findall(r'<a href="(.*?)" title=".*?" target="_blank">.*?</a>',html)
            start_url = 'http://14ckck.com'
            for i in range(len(pageList)):
                new_url = start_url+pageList[i]
                urlList.append(new_url)
        return urlList
    except:
        return"error"

def getText():
    urls = getHtmlList()
    #print(urls)
    # titles = []
    # texts = []
    for each in urls:
        html = getHtmlText(each)
        arttit = re.findall(r'<div class="arttit">(.*?)</div>',html)
        text = re.findall(r'<div>.*?<br>(.*?)<br></div></div>',html)
        arttit1 = str(arttit)
        text1 = str(text).replace('<br>', '\n').replace('\\u3000', ' ')
        with open('%s.txt' % arttit1,'a') as f:
            f.write(str(text1))
            print('正在保存%s.txt '% arttit1)
            f.close()
        # titles.append(arttit)
        # texts.append(text1)
    # # print(titles)
    # # print(texts)
    # for i in range(len(titles)):
    #     with open('%s.txt' % titles[i],'a') as f:
    #         f.write(str(texts[i]))
    #         f.close()

def main():
    #getHtmlList()
    getText()
    print("OK")
main()