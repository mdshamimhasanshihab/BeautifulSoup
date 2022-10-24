import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup
url="https://www.worldometers.info/world-population/bangladesh-population/"
response=requests.get(url)
htmlcontent=response.content
soup=BeautifulSoup(htmlcontent,"html.parser")
# lab_tests=soup.find("div",{"class":"table-responsive"})
# table=lab_tests.find("tr").get_text()
# print(table)
lab_tests=soup.find("tbody")
table=lab_tests.findAll("tr")

year=[]
population=[]
yearly_per_change=[]
yearly_change=[]

merginat=[]
median_age=[]
fertility_rate=[]
density=[]
urban_pop=[]
urban_population=[]
world_pop=[]
world_population=[]
bd_rank=[]

for i in range(len(table)):
    data=table[i].get_text().split(' ')
    year.append(data[1])
    population.append(data[2])
    yearly_per_change.append(data[3])
    yearly_change.append(data[5])
    merginat.append(data[6])
    median_age.append(data[7])
    fertility_rate.append(data[8])
    density.append(data[9])
    urban_pop.append(data[10])
    urban_population.append(data[12])
    world_pop.append(data[13])
    world_population.append(data[15])
    # bd_rank.append(data[15])

    # print(table[i].get_text())
# print(year)
# print(population)
# print(yearly_change)
# print(merginat)
# print(urban_pop)
# # print(bd_rank)
# print('____________________')
# print(data)

# for i in lab_tests:
#     print(i)
# file=open('population.csv','wb')
# writer=csv.writer(file)
# writer.writerow()

row=[[year],[yearly_change],[yearly_per_change]]
dict = {'Year': year, 'Yearly_ChaNGE': yearly_change, 'Yearly_%_Change': yearly_per_change,'Migrant':merginat,'Median_Age':median_age,
        'Fertility_Rate':fertility_rate,'Density':density,'Urban_pop':urban_pop,'Urban_POpulation':urban_population,
        'World_Pop':world_pop,'World_Population':world_population}
df=pd.DataFrame(dict)
df.to_csv('population.csv')
# df=pd.DataFrame(row)
# df.to_csv('pop.csv')

# with open('protagonist.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(row)
