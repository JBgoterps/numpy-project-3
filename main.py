from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

# Page that we will webscrape from
wr_page = 'https://www.pro-football-reference.com/leaders/rec_yds_career.htm'

# Parsing
response = requests.get(wr_page)
wr_soup = BeautifulSoup(response.text, "html.parser")

# Finds table from website
wr_allrows = wr_soup.find("table", {"id":"rec_yds_leaders"}).find("tbody").find_all("tr")
# Shrinks table to first 10 rows
wr_rows = wr_allrows[:10]

# Gets rid of extra characters to make final product cleaner, and puts data into array
players = np.array([row.find_all("td")[0].text.replace("+", "") for row in wr_rows])
yards = np.array([int(row.find_all("td")[1].text.replace(",", "")) for row in wr_rows])

# Sets up two columns: Players and Yards
wr_dic = {
    "Player": players,
    "Yards": yards
}

# Creates CSV
df = pd.DataFrame(wr_dic) 
df.to_csv("nfl_rec_leaders.csv", index=False)
