from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://crewsa-type-residential-session-z7qac1s64qst-sessTimeSecs-7200:aricrew123@proxy.hideiqxshlgvjk.com:5050',
        'https': 'https://crewsa-type-residential-session-z7qac1s64qst-sessTimeSecs-7200:aricrew123@proxy.hideiqxshlgvjk.com:5050',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

driver.get("https://sepolia-faucet.pk910.de/#/mine/a6221e05-900c-46a8-8d0c-20508ecb0e8a")
time.sleep(50000)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
