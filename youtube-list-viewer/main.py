from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import common
import time


def get_timeout(browser):
    try:
        videoLength = str(browser.find_element_by_xpath(
            '//*[@id="movie_player"]/div[31]/div[2]/div[1]/div[1]/span[2]/span[3]/text()'))
    except:
        time.sleep(1)
        get_timeout(browser)

    length = videoLength.split(":")

    if len(length) > 1:
        hour = int(length[0])
        min = int(length[1])
        sec = int(length[2])
    else:
        hour = 0
        min = int(length[0])
        sec = int(length[1])

    hour = hour*60*60
    min = min*60

    timeout = hour + min + sec
    time.sleep(timeout)


def main(url):
    browser = webdriver.Chrome()
    browser.get(url)

    get_timeout(browser)


if __name__ == "__main__":
    common.set_title("Installing ChromeDriver", start="^| ", end=" ^|")
    common.download_chromedriver()

    common.set_title("Starting", start="^| ", end=" ^|")
    urls = common.get_list()

    for url in urls:
        main(url)
