from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://9ac2461b171add92340c__cr.jm:98d0c59cd815a45d@gw.dataimpulse.com:10002',
        'https': 'https://9ac2461b171add92340c__cr.jm:98d0c59cd815a45d@gw.dataimpulse.com:10002',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

driver.get("https://sepolia-faucet.pk910.de/#/mine/84ff7e16-2008-40f0-bff1-1f2dc24a6524")
time.sleep(50000)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
