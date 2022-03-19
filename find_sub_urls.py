from bs4 import BeautifulSoup
from collections import deque
import requests.exceptions
import urllib.parse
import requests
import re


class Scraper:
    def __init__(self, url, limit: int = 100):
        self.user_url = url
        self.urls = deque([self.user_url])
        self.scraped_urls = set()
        self.emails = set()
        self.limit = limit
        self.count = 0

        # self.find_urls()

    def find_urls(self) -> tuple:
        """Find URLs refrenced on input url"""
        while len(self.urls):
            self.count += 1
            if self.count == self.limit:
                break
            url = self.urls.popleft()
            self.scraped_urls.add(url)

            parts = urllib.parse.urlsplit(url)
            base_url = "{0.scheme}://{0.netloc}".format(parts)

            path = url[:url.rfind("/")+1] if "/" in parts.path else url

            # print found urls
            print("[%d] URL: %s" % (self.count, url))
            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                continue

            self.find_emails(response)  # Find emails
            soup = BeautifulSoup(response.text, features="lxml")

            # <A href="">
            for anchor in soup.find_all("a"):
                link = anchor.attrs["href"] if "href" in anchor.attrs else ""
                if link.startswith("/"):
                    link = base_url + link
                elif not link.startswith("http"):
                    link = path + link
                if not link in self.urls and not link in self.scraped_urls:
                    self.urls.append(link)

            # <SPAN href="">
            for anchor in soup.find_all("span"):
                link = anchor.attrs["href"] if "href" in anchor.attrs else ""
                if link.startswith("/"):
                    link = base_url + link
                elif not link.startswith("http"):
                    link = path + link
                if not link in self.urls and not link in self.scraped_urls:
                    self.urls.append(link)
        return self.scraped_urls, self.emails

    def find_emails(self, response):
        """Find emails in requests.text (```r.text```)"""
        new_emails = set(re.findall(
            r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]", response.text, re.I))
        self.emails.update(new_emails)


try:
    url = str(input("[+] Target URL >>> "))
    scraper = Scraper(url, limit=10)
    urls, emails = scraper.find_urls()

    # for url in urls:
    #     print(url)
except KeyboardInterrupt:
    exit(0)
