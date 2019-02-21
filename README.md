# Store chrome plugin

## Install env :
* Add *jquery* minified in vendors folder
* Install Python, pip
```
pip install -r requirements.txt
```
* Run `export FLASK_ENV=development`
* Run `export FLASK_APP=app.py`

Install postgres if you don't have it yet
then `createdb store-plugin` in terminal

## Aviod gitignore silly mistake

don't forget to create vendor folder with jquery-3.3.1 min

## View, use and administrate plugin
-> *Goto* [https://developer.chrome.com/home](https://developer.chrome.com/home) to use and test the plugin

-> *Goto* chrome://extensions/ to administrate plugin

## run the API

`flask run`


### Usefull

https://developer.chrome.com/extensions/devguide
https://developer.chrome.com/extensions/getstarted
