#Import Basic Librarries;-
import os
#!nvidia-smi

HOME = os.getcwd()
print("HOME:", HOME)
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Step 1: Web Scraping for 'SCRAMBLING' Database.
url = 'https://www.livgolf.com/stats/scrambling?season=2024&tournamentId=27&tab=players'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting relevant data
player_data = []
for row in soup.select('.table-row'):
position = row.select_one('.pos').text.strip()
player_name = row.select_one('.player-name').text.strip()
par_or_better = row.select_one('.par-or-btr').text.strip()
scrambling_percentage = row.select_one('.scrambling-percentage').text.strip()

player_data.append({
'Position': position,
'Player Name': player_name,
'Par or Btr': par_or_better,
'Scrambling %': scrambling_percentage
})

# Step 2: Save Data to CSV
df = pd.DataFrame(player_data)
df.to_csv('livgolf_scrambling_stats_2024.csv', index=False)

print("Data saved successfully to 'livgolf_scrambling_stats_2024.csv'!")