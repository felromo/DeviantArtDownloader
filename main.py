#!/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve
from urllib.parse import quote_plus

USER_AGENT = {'User-agent': 'Mozilla/5.0'}

url = ".deviantart.com/gallery/"
user = ""
current_page = ""
links = []
counter = 1


def origin_picture(link):
    # request the page in the passed link
    li = []
    image_request = Request(link, None, USER_AGENT)
    image_page = urlopen(image_request).read()
    soup = BeautifulSoup(image_page)
    pictures = soup.findAll('div', {'class': 'dev-view-deviation'})
    for i in pictures:
        tmp = i.findAll('img')
        for f in tmp:
            li.append((f['src'], f['alt']))
    # parse for .dev-view-deviation
    # get src for 2nd img tag
    return li[0]


def save_picture(link):
    save = open("Downloads/" + str(link[1]), 'wb')
    save.write(urlopen(link[0]).read())
    save.close()
    print(link[1])
    print(link[0])

if __name__ == '__main__':
    user = input("User Name: ")
    url = user + url
    # if there is next page run
    page_request = Request("http://" + url, None, USER_AGENT)
    current_page = urlopen(page_request).read()
    soup = BeautifulSoup(current_page)
    picture_thumbnails = soup.findAll('a', {'class': 'thumb'})
    for i in picture_thumbnails:
        links.append(i['href'])
    for link in links:
        # print(origin_picture(link))
        # pass in touple (url, title)
        save_picture(origin_picture(link))
        # save_picture(link)
