from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = {
    'proxy': {
        'http': 'http://20c7c8a40e451f745708__cr.jm:95babd065f3c22c1@gw.dataimpulse.com:10001',
        'https': 'https://20c7c8a40e451f745708__cr.jm:95babd065f3c22c1@gw.dataimpulse.com:10001',
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

driver.get("https://sepolia-faucet.pk910.de/#/mine/eaf36178-1899-4f23-9cea-a2196d993d5f")
time.sleep(50000)

div_element = driver.find_element(By.CLASS_NAME, "col-3")
content_text = div_element.text
print(content_text)

#WAKTU MENUNGGU MINING SELESAI
time.sleep(15000)

# Tutup browser
driver.quit()
