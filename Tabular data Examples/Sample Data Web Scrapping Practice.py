#Import Basic Librarries;-
import os
#!nvidia-smi

HOME = os.getcwd()
print("HOME:", HOME)
import requests
import pandas as pd
from bs4 import BeautifulSoup
# Define the URL
url = "https://dashboard.dghs.gov.bd/pages/hss_scoring_facility_detail.php?facility_code=10000033&year=2023&month=11&level=5&rank=9#Leadership"

# Send an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the relevant table (you may need to inspect the page source to identify the correct table)
table = soup.find("table")

# Extract table headers
headers = [th.text.strip() for th in table.find_all("th")]

# Initialize an empty list to store rows
rows = []

# Extract table rows
for row in table.find_all("tr")[1:]:
    row_data = [td.text.strip() for td in row.find_all("td")]
    rows.append(row_data)

# Create a DataFrame from the extracted data
df = pd.DataFrame(rows, columns=headers)

# Save the DataFrame to a CSV file
df.to_csv("facility_data.csv", index=False)

print("Data has been successfully scraped and saved to 'facility_data.csv'.")
