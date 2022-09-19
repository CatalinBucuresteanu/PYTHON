
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
path="C:\\Users\Fane\Downloads\chromedriver_win32/chromedriver.exe"
service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)
driver.get("https://demo.anhtester.com/input-form-demo.html")
class automaton:
    def automation(Nume,Prenume,mail,numartelefon,adresa,oras,stat,zipcode,website,text,bool,path1,path2,path3,path4):
        my_elements = driver.find_elements(by="xpath",value=path1)  
        my_elements[0].send_keys(Prenume)
        my_elements[1].send_keys(Nume)
        my_elements[2].send_keys(mail)
        my_elements[3].send_keys(numartelefon)
        my_elements[4].send_keys(adresa)
        my_elements[5].send_keys(oras)
        nouelement=driver.find_elements(by="xpath",value=path2)
        nouelement[stat].click()

        my_elements[6].send_keys(zipcode)
        my_elements[7].send_keys(website)
        my_elements[9].click()

        element=driver.find_element(by="xpath",value=path3)
        element.send_keys(text)
        element=driver.find_element(by="xpath",value=path4)
        element.click()
        time.sleep(10000)
        driver.quit()
obj=automaton.automation("Alin","Gheorghe","test@gmail.com","0712345678","Strada Privighetorilor Numarul 39","Juneau",2,"56255","https://github.com/CatalinBucuresteanu","Automatizare in Selenium",2,"//input","//select//option","//textarea[@class='form-control']","//div[@class='col-md-4']//button")
