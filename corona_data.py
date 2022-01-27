import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from lxml import html
import requests
import os
import wget
import zipfile


try:
    if not os.path.isfile(f"{os.getcwd()}/chromedriver.exe"):
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        response = requests.get(url)
        version_number = response.text

        download_url = "https://chromedriver.storage.googleapis.com/" + \
            version_number + "/chromedriver_win32.zip"

        latest_driver_zip = wget.download(download_url, 'chromedriver.zip')

        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall()
        os.remove(latest_driver_zip)
except Exception as e:
    exit("unable to download chromedriver")


# Standort für inzidenz
ip_data = requests.get("http://ipinfo.io/json").json()
data = requests.get("https://www.whois.com/whois/" + ip_data['ip'])

src = html.fromstring(data.content)
info = src.xpath('//pre[@id="registryData"]/text()')

addresses = list()
for line in info:
    lines = line.split("\n")
    for line in lines:
        if str(line).__contains__("address"):
            addresses.append(line.replace("address:        ", ""))


# Inzidenz
options = Options()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get(
    f"https://www.corona-in-zahlen.de/landkreise/sk%20{addresses[4].split(',')[0]}/")

time.sleep(3)
corona_info_src = html.fromstring(driver.page_source)
driver.close()


corona_info = corona_info_src.xpath('//p[@class="card-title"]//text()')
print(f"""CORONA INFO ---> {addresses[4].split(',')[0]}
_________________________________
Einwohner: {corona_info[0]}
Infektionen(gesamt): {corona_info[1]}
Infektionsrate(gesamt): {corona_info[2]}
Neuinfektionen(7-Tage-Inzidenz): {corona_info[3]}
Todesfälle(gesamt): {corona_info[4]}
Letalitätsrate(gesamt): {corona_info[5]}
Intensivmedizinisch behandelte COVID-19 Patienten: {corona_info[6]}
Invasiv beatmete COVID-19 Patienten: {corona_info[7]}
Anteil COVID-19 Patienten an Intensivbetten: {corona_info[8]}
""")
