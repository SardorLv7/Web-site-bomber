#!usr/bin/env python
import requests

def request(url):
    try:
        return requests.get("https://" + url)
        print(get_response)
    except requests.exceptions.ConnectionError:
        pass

target_url = "http://oxu.uz"

with open("/home/kali/Downloads/subdomains-10000.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        target_line = target_url + "/" + word
        response = request(target_line)
        if response:
            print("we havee >>>> " + target_line)