from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import time
import csv
import requests
from docx import Document
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# query = input('Key Word: ')

list_song_url=[
"https://open.spotify.com/track/6ogEumu8wnKzCPq2uGdb5x",
"https://open.spotify.com/track/1v1oIWf2Xgh54kIWuKsDf6",
"https://open.spotify.com/track/1UWacd8x8tPPwmrPB1MoBI",
"https://open.spotify.com/track/2AB7fsbG0eZJjDGile69CQ",
"https://open.spotify.com/track/39EWLnXojnOtZHYKBpewtL",
"https://open.spotify.com/track/33aLws184a7SVqraKuDqI3",
"https://open.spotify.com/track/6GD1eomgaGT1Epto6Q5eAo",
"https://open.spotify.com/track/1M26YHUrrERZ1ya2LgkGpw",
"https://open.spotify.com/track/7Ai5pAx4S93BJsZnaLdTnf",
"https://open.spotify.com/track/1l1Tv0NFhRQQHIO2UFgYdJ",
"https://open.spotify.com/track/5cqoXFUFSCO1RirYcOZu7G",
"https://open.spotify.com/track/5SuOikwiRyPMVoIQDJUgSV",
"https://open.spotify.com/track/2gQPv5jvVPqU2a9HhMNO1v",
"https://open.spotify.com/track/4ZtFanR9U6ndgddUvNcjcG",
"https://open.spotify.com/track/6HU7h9RYOaPRFeh0R3UeAr",
"https://open.spotify.com/track/5wANPM4fQCJwkGd4rN57mH",
"https://open.spotify.com/track/6N1K5OVVCopBjGViHs2IvP",
"https://open.spotify.com/track/1smFN2CLqGROu0J0UyvDfL",
"https://open.spotify.com/track/56zZ48jdyY2oDXHVnwg5Di",
"https://open.spotify.com/track/7wMPhUSe6CZga1vOMpLTJP",
"https://open.spotify.com/track/550rQQCGkrTzvp4SfpOPzx",
"https://open.spotify.com/track/4mnjwMLCk3JZkhkok3u5g1",
"https://open.spotify.com/track/3IxMaULfjq4IT2IN6v54PB",
"https://open.spotify.com/track/3z9OnsnvM6SFN2dzrSDdVO",
"https://open.spotify.com/track/71KaNgCTNC2J5foUoO06wF",
"https://open.spotify.com/track/4btFHqumCO31GksfuBLLv3",
"https://open.spotify.com/track/7pKfPomDEeI4TPT6EOYjn9",
"https://open.spotify.com/track/7qEHsqek33rTcFNT9PFqLf",
"https://open.spotify.com/track/5a6QRq732nUdlxnKHmQbHa",
"https://open.spotify.com/track/3IHHqmfKJHyI0obINUdg1W",
"https://open.spotify.com/track/3ZffCQKLFLUvYM59XKLbVm",
"https://open.spotify.com/track/5GorCbAP4aL0EJ16frG2hd",
"https://open.spotify.com/track/7ce20yLkzuXXLUhzIDoZih",
"https://open.spotify.com/track/4SSnFejRGlZikf02HLewEF",
"https://open.spotify.com/track/53W8zd1F4QASq67PsllYOG",
"https://open.spotify.com/track/0KAFjeQ6jpmtKP4CW9m5X6",
"https://open.spotify.com/track/3SHg4VamqiJkGSU5o4zEaD",
"https://open.spotify.com/track/0vIdtGA9yNvcAZ3mloGfzH",
"https://open.spotify.com/track/1nsn93tZ1aUhsEbNETgkvH",
"https://open.spotify.com/track/4Cd01GWLuMTNZhW0DE7cF4",
"https://open.spotify.com/track/4TOm61nHo2nVsXRJVcYkag",
"https://open.spotify.com/track/6UthgbZgkrh7dYQzFqYMLA",
"https://open.spotify.com/track/7eJMfftS33KTjuF7lTsMCx",
"https://open.spotify.com/track/4xqrdfXkTW4T0RauPLv3WA",
"https://open.spotify.com/track/14PO4TmZLQX3gJoVoiAPfb",
"https://open.spotify.com/track/4VuS959DSpr82t3qBqCrWG",
"https://open.spotify.com/track/3AHWbUsTaYecnT4aTEU0ut",
"https://open.spotify.com/track/1MncJkUEvrcTYhGEdOkUjF",
"https://open.spotify.com/track/3fToxtMS9O52sP4ZTV5yqm",
"https://open.spotify.com/track/561jH07mF1jHuk7KlaeF0s",
"https://open.spotify.com/track/1v7L65Lzy0j0vdpRjJewt1",
"https://open.spotify.com/track/0SuG9kyzGRpDqrCWtgD6Lq",
"https://open.spotify.com/track/1AI7UPw3fgwAFkvAlZWhE0",
"https://open.spotify.com/track/0afhq8XCExXpqazXczTSve",
"https://open.spotify.com/track/34gCuhDGsG4bRPIf9bb02f",
"https://open.spotify.com/track/1HNkqx9Ahdgi1Ixy2xkKkL",
"https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3",
"https://open.spotify.com/track/0tgVpDi06FyKpA1z0VMD4v",
"https://open.spotify.com/track/6ocbgoVGwYJhOv1GgI9NsF",
"https://open.spotify.com/track/4HBZA5flZLE435QTztThqH",
"https://open.spotify.com/track/3yfqSUWxFvZELEM4PmlwIR",
"https://open.spotify.com/track/4xkOaSrkexMciUUogZKVTS",
"https://open.spotify.com/track/7FIWs0pqAYbP91WWM0vlTQ",
"https://open.spotify.com/track/3W1uF2c1vGAkZegtxIL42e",
"https://open.spotify.com/track/0oTaTGcMhxdTFotrPnHYwr",
"https://open.spotify.com/track/6lanRgr6wXibZr8KgzXxBl",
"https://open.spotify.com/track/7129iqBafaphfc3WPCGC0L",
]

ask = input("Google/Edge:\t")

if ask == "g":
    start_url = "https://www.google.com/"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

else:
    start_url = "https://www.bing.com/"
    browser = webdriver.Edge(EdgeChromiumDriverManager().install())

browser.get(start_url)

time.sleep(2.5)

data = []       # Will store all the urls after finding

song = []
composer = []

# Will Search urls for the topic in the browser and take the text part of each page
def scrape(idx, query):

    browser.get(query)
    time.sleep(2.5)

    Soup = BeautifulSoup(browser.page_source, "html.parser")

    temp_song = []
    temp_comp = []

    os.system("CLS")

    for data in Soup(['h1']):
        temp_song.append(data.get_text())

    for data2 in Soup(['h2']):
        temp_comp.append(data2.get_text())

    song.append(temp_song[0])
    composer.append(temp_comp[1])

    print(idx+1)


os.system("CLS")
add_songs = 0
error_songs = []

# for i in range(6):
for i in range(len(list_song_url)):
    scrape(i,list_song_url[i])

with open("song_list.txt","w+") as f:
    for i in range(len(song)):
        try:
            f.write(f"{song[i]} by {composer[i]}")
            f.write("\n")
            add_songs+=1
        except:
            print(f"{song[i]} by {composer[i]}")
            error_songs.append(f"{song[i]} by {composer[i]}")
            pass

print("\n\n\n\n\n\n")
browser.close()
input('exit...')
exit()
