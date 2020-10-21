import sys
import urllib.request
import urllib.parse

import bs4
from bs4 import BeautifulSoup

def contains(source, tag):
    return source.find(tag, 0, len(source)) > -1

def containsAny(source, tags):
    for tag in tags:
        if source.find(tag, 0, len(source)) > -1:
            return True
    return False

if __name__ == '__main__':
    url = 'http://data.acmr.com.cn/member/city/city_md.asp'
    f = urllib.request.urlopen(url)

    str = f.read().decode('gb2312')
    # print(str)

    sys.setrecursionlimit(2000)
    soup = BeautifulSoup(str, 'html.parser')
    # // maintext
    allATag = soup.find_all('a')
    # print(len(allATag))
    allProvince = []
    provinceTags = ['北京市', '天津市', '内蒙',  '上海市', '广西', '重庆市', '宁夏', '新疆', '省']
    for aTag in allATag:
        isString = type(aTag.string) is bs4.element.NavigableString
        if bool(1-isString):
            continue
        # print(aTag.string)
        isProvince = containsAny(aTag.string, provinceTags)
        if bool(1-isProvince):
            continue
        print(aTag.string)
        allProvince.append(aTag.string)
    allProvince = list(set(allProvince))
    print(len(allProvince))

