from asyncio import constants
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
website ="https://www.bonprix.ro/categorie/394/camasi-barbati/?sortOrder=3"
path="C:\\Users\Fane\Downloads\chromedriver_win32/chromedriver.exe"
options=Options()
options.headless=True
service=Service(executable_path=path)
driver=webdriver.Chrome(service=service,options=options)
driver.get(website)
containers=driver.find_elements(by="xpath",value='//div[@id="product-list"]//p[@class="thumbnail loaded"]//img')
titles=[]
container=containers[0]
for i  in range(0,len(containers)):
    titles.append(containers[i].get_attribute("alt"))
        

my_dict={'titles': titles}
df_headlines=pd.DataFrame(my_dict)

df_headlines.to_csv("bonprix.csv")
driver.quit()