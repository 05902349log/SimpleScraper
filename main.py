import json
import httpx
from selectolax.parser import HTMLParser
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")
header = os.getenv("HEADER")


def main():
    with open("MangaTitle.json") as f:
        d = json.load(f)

    headers = {"User-Agent": header}

    resp = httpx.get(url, headers=headers)

    html = HTMLParser(resp.text)

    # To find css class use ".<Item>"
    # To find css id use "#<Item>"
    pageData = html.css("div.uta div.luf")

    latestUpdatedList = []

    for manga in pageData:
        mangaObj = {
            "mangaName": manga.css_first(".series").text().replace("\n", "").replace("’", "'"),
            "mangaChapter": manga.css_first("li a").text(),
            "last_updated": manga.css_first("li span").text(),
        }

        if mangaObj["mangaName"] in d["Titles"]:
            latestUpdatedList.append(mangaObj)
            print(f"Manga name: {mangaObj["mangaName"]}")
            print(f"Last updated: {mangaObj["last_updated"]}\n")

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
