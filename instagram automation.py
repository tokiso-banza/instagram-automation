# 以前のセッションのクッキーを読み込む
from selenium import webdriver

import time
from selenium.webdriver.common.by import By

import pickle

with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)

driver = webdriver.Chrome()

# ウェブサイトにアクセス
driver.get('https://www.instagram.com/')

# クッキーをブラウザにセット
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)

# 彩度ウェブサイトにアクセス
driver.get('https://www.instagram.com/')

time.sleep(5)  # ページが完全にロードされるのを待つ

try:
    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div/svg")
    login_button.click()
except:
    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div")
    login_button.click()
time.sleep(5)
try:
    username = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
    username.send_keys('留学生') # 実際のユーザー名を入力
except:
    username = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
    username.send_keys('留学生') # 実際のユーザー名を入力
time.sleep(5)

try:
    login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div")
    login_button.click()
except:
    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div")
    login_button.click()
time.sleep(5)

try:
    login_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button")
    login_button.click()
except:
    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button")
    login_button.click()

driver.quit()