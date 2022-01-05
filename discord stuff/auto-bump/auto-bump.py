from datetime import datetime
from colorama import Fore
import requests
import random
import json
import time
import os


def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers


def proxy_scrape():
    startTime = time.time()
    temp = os.getenv("temp")+"\\proxies.txt"
    print(f"{Fore.YELLOW}Scraping Proxyies")
    r = requests.get(
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=8500&country=all&ssl=all&anonymity=elite&simplified=true", headers=getheaders())
    with open(temp, "wb") as f:
        f.write(r.content)
    execution_time = (time.time() - startTime)
    print(f"{Fore.GREEN}Done scraping proxies => {temp}{Fore.RESET} | {execution_time}ms")


def proxy():
    temp = os.getenv("temp")+"\\proxies.txt"
    if not os.path.exists(temp):
        with open(temp, "w") as f:
            f.close()
    if os.stat(temp).st_size == 0:
        proxy_scrape()
    proxies = open(temp).read().split('\n')
    proxy = proxies[1]

    with open(temp, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])
        os.system("cls;clear")
    return proxy


with open("./bd-config.json", "r") as f:
    data = json.load(f)


count = 1
os.system("cls")
while 1:
    try:
        token = data["token"]

        r = requests.get('https://discord.com/api/v9/users/@me',
                         proxies={"ftp": f'{proxy()}'},
                         headers=getheaders(token))

        userName = r.json()['username']
        userID = r.json()['id']
        space = "".join(" " for i in range(19 - len(userName)))

        for channelID in data["channelID"]:
            headers = {'Authorization': token}
            requests.post(f'https://discord.com/api/v9/channels/'+channelID+'/messages',
                          proxies={"ftp": f'{proxy()}'},
                          headers=headers,
                          data={"content": f"!d bump"})

            timeout = random.randint(5, 30)
            ct = time.strftime('%H:%M:%S').split(':')
            print(
                f"{userName}{space}|   {channelID}   |   !d bump ┈>  {str(count)}   |   Next Bump ┈>  {str(int(ct[0])+2)}:{str(ct[1])}:{str(int(ct[2])+timeout)}")
        time.sleep(int(data["timeout"]) + timeout)
        count += 1
    except:
        print("Auth/Bump failed ┈>  retrying in 1min 40sec")
        time.sleep(100)
