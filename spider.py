#!usr/bin/env python
import re
import requests
import urlparse


target_url = "https://odamlar.tv"
target_list = []

def exact_links(url):
    response = requests.get(target_url)
    return re.findall(b'(?:href=")(.*?)"', response.content)

def crawler(url):
    href_links = exact_links(url)

    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#"[0])
        if target_url in link and link not in target_list:
            target_list.append(link)
            print(link)
            crawler(link)
crawler(target_url)
