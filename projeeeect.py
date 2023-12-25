from bs4 import BeautifulSoup
import requests
import csv
import os

info = ["Name", "Studio", "Year", "Rate", "Episodes"]
csvfile = open('movie_data.csv', 'w', newline='') 
csvwriter = csv.writer(csvfile)
csvwriter.writerow(column_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0'
}

website = requests.get('https://anilist.co/search/anime?genres=Detective', headers=headers).text
soup = BeautifulSoup(website, 'lxml')
#animes = soup.find_all('li', class_= '<div data-v-219025ae class="results cover">grid')
i = 0

for anime in animes:
    #name = anime.find('h3', class_= 'ipc-title__text').text.split('. ')[1:]
    name = "{}".format(*name) 
    
#sadac weria "#" - davibeni da ar vici ra gavaketo
#am etapze vsio
#arc vici ra gavaketo
#mishvelet!!!