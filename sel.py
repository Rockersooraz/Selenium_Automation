from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/Users/suraj.adhikari/Downloads/chromedriver.exe')
driver.get('https://www.seleniumhq.org/')
driver.find_element_by_link_text('Download')
elem = driver.find_element_by_link_text('Projects')
elem.click()
down=driver.find_element_by_link_text('Download')
down.click()
searchBar = driver.find_element_by_id('q')
searchBar.send_keys('automate')
from selenium.webdriver.common.keys import Keys 
searchBar.send_keys(Keys.ENTER)