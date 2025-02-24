from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def setup_driver():
    options = {
        'proxy': {
            'http': 'http://sodagar:FGAMRHJ-QQHC7SJ-0RPJ3H1-BOMNLIP-WKACAQO-GWSCKMZ-SET2MG4@unmetered.residential.proxyrack.net:10011',
            'https': 'https://sodagar:FGAMRHJ-QQHC7SJ-0RPJ3H1-BOMNLIP-WKACAQO-GWSCKMZ-SET2MG4@unmetered.residential.proxyrack.net:10011',
            'no_proxy': 'localhost,127.0.0.1'
        }
    }

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--verbose")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920, 1200")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("--disable-client-side-phishing-detection")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-features=NetworkPrediction")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--metrics-recording-only")
    chrome_options.add_argument("--safebrowsing-disable-auto-update")
    chrome_options.add_argument("--disable-component-update")
    chrome_options.add_argument("--disable-domain-reliability")

    driver = webdriver.Chrome(seleniumwire_options=options, options=chrome_options)
    return driver

def main():
    driver = setup_driver()
    driver.get("https://sepolia-faucet.pk910.de/#/mine/aadb9164-d687-4aef-9e5e-ef0cb7cd1ccb")

    while True:
        try:
            # Tunggu hingga halaman sepenuhnya dimuat
            time.sleep(30)  # Sesuaikan waktu tunggu sesuai kebutuhan

            # Cek apakah elemen yang diinginkan ada
            div_element = driver.find_element(By.CLASS_NAME, "col-3")
            content_text = div_element.text
            print(content_text)

            # Tunggu 15 menit sebelum refresh
            time.sleep(1800)

            # Refresh browser
            driver.refresh()

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            # Jika terjadi kesalahan, tutup browser dan buka kembali
            driver.quit()
            driver = setup_driver()
            driver.get("https://sepolia-faucet.pk910.de/#/mine/aadb9164-d687-4aef-9e5e-ef0cb7cd1ccb")

if __name__ == "__main__":
    main()
