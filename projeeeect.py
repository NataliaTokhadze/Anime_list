from bs4 import BeautifulSoup
import requests
import csv
import os
import lxml

info = ["Name", "Year", "Rate", "Studio", "Episodes"]
csvfile = open('movie_data.csv', 'w', newline='') 
csvwriter = csv.writer(csvfile)
csvwriter.writerow(info)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0'
}

website = requests.get('https://anilist.co/search/anime?genres=Detective', headers=headers).text
soup = BeautifulSoup(website, 'lxml')
animes = soup.find_all('div', class_= "media-card")
i = 0

for anime in animes:
    name = anime.find('a', class_= 'title').text.split('. ')[1:]
    name = "{}".format(*name)
     
    
    movie_data = anime.find_all('div', class_='header')
    year = movie_data[0].text
    rating = movie_data[1].text
    
    studio = anime.find('div', class_='studios')
    
    information = anime.find('div', class_ = 'info')
    episode = information[2].text 
    
    i += 1

    csvwriter.writerow([i, name, year, rating, studio, episode])
    
print(f"Done writing {i} entries to the csv file!")
csvfile.close()
