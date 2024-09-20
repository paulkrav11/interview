import requests
from bs4 import BeautifulSoup

url = 'https://terrikon.com/football/italy/championship/strikers'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', class_='colored')

html_table = "<table><th></th><th>Игрок</th><th>Команда</th><th>Забито</th><th>Пенальти</th><th>Игр</th><th>Среднее</th>"

for i, row in enumerate(table.find_all('tr')[1:]):
    columns = row.find_all('td')
    place = i + 1
    player = columns[1].a.text  
    team = columns[2].a.text  
    goals = columns[3].text
    penalties = columns[4].text
    games = columns[5].text
    average = columns[6].text

    html_table += f"<tr><td>{place}.</td><td>{player}</td><td>{team}</td><td>{goals}</td><td>{penalties}</td><td>{games}</td><td>{average}</td></tr>"

html_table += "</table>"

print(html_table)