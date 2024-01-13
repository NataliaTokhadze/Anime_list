from bs4 import BeautifulSoup
import requests
import csv
import os
import lxml

info = ["Name", "Year", "Episodes", "Rate"]
csvfile = open('movie_data.csv', 'w', newline='', encoding='utf-8') 
csvwriter = csv.writer(csvfile)
csvwriter.writerow(info)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0'
}

website = requests.get('https://myanimelist.net/anime/genre/39/Detective?fbclid=IwAR2odpgA-cfDUtTsEogW1sxevTINeldDFlXJpo5mdjAkhju5nt5RgRuRY78', headers=headers).text
soup = BeautifulSoup(website, 'lxml')
animes = soup.find_all('div', class_= 'js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1')
i = 0

for anime in animes:
    name = anime.find('a', class_= 'title').text.split('. ')[1:]
    name = "{}".format(*name)
    
    movie_data = anime.find_all('div', class_='info')
    year = movie_data[0].text
    episode = movie_data[2].text
    
    information= anime.find('div', class_= 'information')
    rating = information[0].text 
    
    i += 1

    csvwriter.writerow([i, name, year, episode, rating])
    
print(f"Done writing {i} entries to the csv file!")
csvfile.close()
