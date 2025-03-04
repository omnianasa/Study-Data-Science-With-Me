# Import all libraries will be needed
import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
table = soup.find("table", class_="wikitable")  

# extract all rows in the table
rows = table.find_all("tr")

data = []
# print the extracted rows
for row in rows:
    cells = row.find_all(["td", "th"])
    row_data = [cell.get_text(strip=True) for cell in cells]
   
    if row_data:
        data.append(row_data)

df = pd.DataFrame(data)
df.columns = df.iloc[0]
df.rename(columns = {"Economics(The Sveriges Riksbank Prize)[13][a]":"Economics"}, inplace = True)
df = df[1:]
print(df.head(3))
df.to_csv('NobelPrizes.csv', index=False)








