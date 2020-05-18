# scopus_app

## Description

Application, in which the user can log into scopus (must have account on www.scopus.com) and searches a query (chooses its settings in UI)

Analyzes documents from query, and returns the results.

When analyzing is finished, an Excel file is exported, containing all the dictionaries mentioned above (documents with its info)

### Works for

1. Journal Sources
2. Conference Proceedings Sources
3. Book Series Sources

### Doesn't work for

1. Book Sources (yet)

## Prerequisites

1. Python 3.7
2. Correct version chromedriver (depends on your version of Chrome, for more see http://chromedriver.chromium.org/)
3. If using Windows, please add Chromedriver in PATH (for more see https://www.computerhope.com/issues/ch000549.htm)

## Requirements

```
pip install -r requirements.txt
```

### NOTE!

I haven't tested in other browser drivers, rather than Chrome

## Usage

### Client

```
python main.py
```

### Server

```
python server.py
```
