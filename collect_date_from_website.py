import random
import time

import bs4
import requests
'''
Get github IP
'''

def read_file(path):
    hostmap = {}
    try:
        with open(path,mode='r',encoding='utf-8') as f:
            for line in f:
                if line.endswith('com\n'):
                    strs = line.split(' ')
                    if len(strs)==2:
                        hostmap[strs[1][:-1]] = strs[0] #[:-1] 去掉结尾的换行符 \n
                    if len(strs)==1:
                        hostmap[strs[0][:-1]] = ''  #[:-1] 去掉结尾的换行符 \n
        return hostmap
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')

def main(hostmap):
    urlmaps={}
    for url,ip in hostmap.items():
        resp = requests.get(
            url=f'https://websites.ipaddress.com/{url}',
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/83.0.4103.97 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;'
                          'q=0.9,image/webp,image/apng,*/*;'
                          'q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            },
        )
        #print(resp.encoding)
        resp.encoding = 'utf-8'
        soup = bs4.BeautifulSoup(resp.text,'html.parser')
        #print(soup)
        #elements = soup.select('body > div.resp.main > main > section:nth-child(8) > table > tbody > tr:nth-child(1) > td > div > ul > li:nth-child(1) > strong')
        elements = soup.select('body > div.resp.main > main > section:nth-child(4) > table > tbody > tr:nth-child(7) > td > ul > li')
        if(len(elements))==0:
            elements = soup.select('body > div.resp.main > main > section:nth-child(8) > table > tbody > tr:nth-child(1) > td > div > ul > li:nth-child(1) > strong')
        if (len(elements)) == 0:
            elements = soup.select('body > div.resp.main > main > section:nth-child(4) > table > tbody > tr:nth-child(3) > td > ul')
        if (len(elements)) == 0:
            elements = soup.select('body > div.resp.main > main > section:nth-child(4) > table > tbody > tr:nth-child(3) > td > ul > li')
        if (len(elements)) == 0:
            elements = soup.select('body > div.resp.main > main > section:nth-child(8) > table > tbody > tr:nth-child(9) > td > div > ul > li:nth-child(1) > strong')
        if (len(elements)) == 0:
            elements = soup.select('body > div.resp.main > main > section:nth-child(8) > table > tbody > tr:nth-child(1) > td > div > ul > li:nth-child(1) > strong')
        if (len(elements)) == 0:
            elements = soup.select('body > div.resp.main > main > section:nth-child(8) > table > tbody > tr:nth-child(1) > td > div > ul > li:nth-child(1) > strong')

        if(len(elements))==0:
            print(url)
        for element in elements:
            print(element.get_text() + " " + url)
            urlmaps[url] = element.get_text()
        #time.sleep(1)

    print(urlmaps)


if __name__ == '__main__':
    hostmap = read_file('/etc/hosts')
    print('read /exc/hosts:' + str(hostmap))
    main(hostmap)