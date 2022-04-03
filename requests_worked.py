import threading
import requests
import _thread
import json
import time

threads = []
worked = 0
failed = 0
x = 50


def req():
    global worked, failed
    r = requests.get("http://localhost:5000")
    content = r.content.decode("utf-8")  # .replace("{", "").replace("}", "")
    res = json.loads(content)

    if res["succsess"]:
        worked += 1
    else:
        failed += 1


def main():
    global worked, failed
    for i in range(x):
        t = threading.Thread(target=req)
        time.sleep(0.1)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == "__main__":
    _thread.start_new_thread(main, ())
    while 1:
        print(
            f"\rWorked: {worked+1}   |   Failed: {failed}   |   Total: {worked+failed+1}", end="\r")
        if worked+failed == x:
            print("\n")
            break
