from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://d8e500d03fdb94e45fc4__cr.mx:5d58840656e914d2@gw.dataimpulse.com:10014',
        'https': 'https://d8e500d03fdb94e45fc4__cr.mx:5d58840656e914d2@gw.dataimpulse.com:10014',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--verbose")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920, 1200")
# Hapus '--headless' untuk melihat apakah ekstensi berjalan dengan benar dalam mode normal
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-background-networking")  # Mencegah koneksi jaringan di latar belakang
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--disable-client-side-phishing-detection")  # Nonaktifkan deteksi phishing
chrome_options.add_argument("--disable-default-apps")  # Nonaktifkan aplikasi bawaan Chrome
chrome_options.add_argument("--disable-features=NetworkPrediction")  # Nonaktifkan prediksi jaringan
chrome_options.add_argument("--disable-sync")  # Nonaktifkan sinkronisasi
chrome_options.add_argument("--metrics-recording-only")  # Nonaktifkan pengumpulan data
chrome_options.add_argument("--safebrowsing-disable-auto-update")  # Nonaktifkan pembaruan otomatis Safe Browsing
chrome_options.add_argument("--disable-component-update")  # Nonaktifkan pembaruan komponen
chrome_options.add_argument("--disable-domain-reliability")  # Nonaktifkan keandalan domain

driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)

driver.get("https://sepolia-faucet.pk910.de/#/mine/9f2af854-b51a-4a36-9bb1-59b5cd9d8d78")
time.sleep(50)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
