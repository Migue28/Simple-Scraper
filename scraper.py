from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get('https://www.flipkart.com/computers/laptops/pr?sid=6bo,b5g&otracker=categorytree')
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
#Find data and insert to array
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
#Save data to csv file
data = {'Name': products, 
        'Price': prices, 
        'Rating': ratings}
df = pd.DataFrame(data, columns=['Name', 'Price', 'Rating'])
df.to_csv('simple_scraper.csv', index=False, header=True)
