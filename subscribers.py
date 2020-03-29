import requests

from bs4 import BeautifulSoup

# url = 'https://www.youtube.com/channel/UCFFbwnve3yF62-tVXkTyHqg'

def subscriber(url):
    page = requests.get(url)
    print(page)

    soup = BeautifulSoup(page.text, "html.parser")
    print(soup)
    pew = soup.findAll('span',
                       {'class': 'yt-subscription-button-subscriber-count-branded-horizontal subscribed yt-uix-tooltip'})
    print(pew)

    for subs in pew:
        print("Innovate Yourself subscribers: ",subs.get_text())

    return subs.get_text()
