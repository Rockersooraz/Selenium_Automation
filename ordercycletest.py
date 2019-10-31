from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import os
import subprocess

driver = webdriver.Chrome(executable_path='C:/Users/suraj.adhikari/Downloads/chromedriver.exe')
driver.get('http://192.168.50.61/tms')
driver.maximize_window()

driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div[2]/form/div[1]/input').send_keys('admin')
driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys('Tms@123')
driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div[2]/form/input').click()


wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/app-menubar/aside/nav/ul/li[9]/a/span/span'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/app-menubar/aside/nav/ul/li[9]/ul/li[1]/a/span'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[1]/div[2]/app-three-state-toggle/div/div/label[3]'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/input'))).send_keys('API')
act = ActionChains(driver)
act.send_keys(Keys.CONTROL).send_keys("a").perform()

#wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/input'))).send_keys('API')
