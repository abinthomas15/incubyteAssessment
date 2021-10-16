import csv
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.newegg.ca/GIGABYTE-AMD-Motherboards/BrandSubCat/ID-1314-22')
soup = BeautifulSoup(source.text,'html.parser')

csv_file = open('scraped.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Motherboard_Name','Old_Price','New_Price'])

for title in soup.find_all('div',class_='item-container'):

    label = title.find('a',class_='item-title').text

    print(label)

    try:
        old_price = title.find('li',class_='price-was').span.text
    except:
        old_price = None
    
    print(old_price)

    new_price = title.find('li',class_='price-current').text.split('(')[0]

    print(new_price)

    csv_writer.writerow([label,old_price,new_price])

csv_file.close()


