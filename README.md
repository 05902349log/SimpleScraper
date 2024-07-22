# SimpleScraper

Simple cli web scraper to get latest update of specific manga titles without having to physically go on to the website to check

**Sample JSON file format for storing manga titles**
```
{
  "Titles": ['Title one', 'Title Two','Title Three', ...]
}
```

**Raw result**
```
{'mangaName': 'Title one', 'mangaChapter': 'Chapter 121', 'last_updated': '24 hours ago'}
{'mangaName': 'Title Two', 'mangaChapter': 'Chapter 92', 'last_updated': '2 days ago'}
{'mangaName': 'Title Three', 'mangaChapter': 'Chapter 42', 'last_updated': '3 days ago'}
{'mangaName': 'Title Four', 'mangaChapter': 'Chapter 83', 'last_updated': '4 days ago'}
{'mangaName': 'Title Five', 'mangaChapter': 'Chapter 34', 'last_updated': '4 days ago'}
```
**Sample result**
```
Manga name: Title one
Last updated: 9 hours ago

Manga name: Title two
Last updated: 16 hours ago

Manga name: Title three
Last updated: 2 days ago
```

**Install requirements**
```
pip install -r requirements.txt
```
