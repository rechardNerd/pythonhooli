import random
import time

import bs4
import requests
'''
Get github IP
'''
hosts = [
    'github.com',
    'nodeload.github.com',
    'api.github.com',
    'codeload.github.com',
    'raw.github.com',
    'training.github.com',
    'assets-cdn.github.com',
    'documentcloud.github.com',
    'help.github.com',
    'githubstatus.com',
    'github.global.ssl.fastly.net',
    'raw.githubusercontent.com',
    'pkg-containers.githubusercontent.com',
    'cloud.githubusercontent.com',
    'gist.githubusercontent.com',
    'marketplace-screenshots.githubusercontent.com',
    'repository-images.githubusercontent.com',
    'user-images.githubusercontent.com',
    'desktop.githubusercontent.com',
    'avatars.githubusercontent.com',
    'avatars0.githubusercontent.com',
    'avatars1.githubusercontent.com',
    'avatars2.githubusercontent.com',
    'avatars3.githubusercontent.com',
    'avatars4.githubusercontent.com',
    'avatars5.githubusercontent.com',
    'avatars6.githubusercontent.com',
    'avatars7.githubusercontent.com',
    'avatars8.githubusercontent.com'
]

for url in hosts:
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
    #time.sleep(1)