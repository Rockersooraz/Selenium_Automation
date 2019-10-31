from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/Users/suraj.adhikari/Downloads/chromedriver.exe')
driver.get('http://192.168.50.61/tms')
driver.maximize_window()



driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div[2]/form/div[1]/input').send_keys('admin')
driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys('Tms@123')
driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div[2]/form/input').click()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/app-menubar/aside/nav/ul/li[5]/a/span/span'))).click()

flag = driver.find_element(By.XPATH, '/html/body/app-root/tms/app-menubar/aside/nav/ul/li[5]/ul/li[6]/a/span')
driver.execute_script("arguments[0].scrollIntoView();", flag)

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/app-menubar/aside/nav/ul/li[5]/ul/li[6]/a/span'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/app-menubar/aside/nav/ul/li[5]/ul/li[6]/ul/li/a'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/main/div/div/app-dna-login/div[2]/div/div[1]/form/div[2]/select'))).send_keys('110')
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/main/div/div/app-dna-login/div[2]/div/div[1]/form/div[3]/input'))).send_keys('Tms@1234567')
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/tms/main/div/div/app-dna-login/div[2]/div/div[1]/form/button[1]'))).click()




