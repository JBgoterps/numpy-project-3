from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

wr_page = 'https://www.pro-football-reference.com/leaders/rec_yds_career.htm'

response = requests.get(wr_page)
wr_soup = BeautifulSoup(response.text, "html.parser")

wr_allrows = wr_soup.find("table", {"id":"rec_yds_leaders"}).find("tbody").find_all("tr")
wr_rows = wr_allrows[:10]

players = np.array([row.find_all("td")[0].text.replace("+", "") for row in wr_rows])
yards = np.array([int(row.find_all("td")[1].text.replace(",", "")) for row in wr_rows])

wr_dic = {
    "Player": players,
    "Yards": yards
}

df = pd.DataFrame(wr_dic) 
df.to_csv("nfl_rec_leaders.csv", index=False)