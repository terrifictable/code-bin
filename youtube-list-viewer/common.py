import requests
import zipfile
import wget
import os


def download_chromedriver() -> str:
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
                # print("Chromedriver installed")
            os.remove(latest_driver_zip)
    except Exception as e:
        return e


def set_title(title, start="", end="") -> None:
    try:
        os.system("title {} {} {}".format(start, title, end))
    except Exception as e:
        return e


def openList(path) -> list:
    with open(path, "r") as f:
        urls = f.readlines()
    return urls


def get_list(path="list.txt") -> list:
    urls = dict()
    try:
        urls = openList(path)
    except:
        for file in os.listdir('.'):
            if not os.path.isfile(file):
                path = os.path.join('.', file)
                try:
                    urls = openList(path)
                except:
                    pass
    return urls
