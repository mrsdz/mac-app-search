"""This module is for parsing arguments"""
import urllib
import requests
import bs4
import arguments

ARGS = arguments.ARGS

def macneed_search(name):
    """Return download link of app"""
    name = urllib.quote_plus(name)
    url = "http://macneed.ir/?s="+name
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.content, "lxml")
    last_version_of_app = soup.find("div", "title_post")
    if last_version_of_app:
        app_link = last_version_of_app.h2.a['href']
        req = requests.get(app_link)
        soup = bs4.BeautifulSoup(req.content, "lxml")
        dl_link = soup.find("a", "green")['href']
        return dl_link
    else:
        return "Sorry, app not found on macneed.ir :("


def version(name):
    """Return version of app"""
    name = urllib.quote_plus(name)
    url = "http://macneed.ir/?s="+name
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.content, "lxml")
    last_version_of_app = soup.find("div", "title_post")
    if last_version_of_app:
        app_version = last_version_of_app.h2.a.string
        return app_version
    else:
        return "Sorry, app not found on macneed.ir :("


if ARGS.version:
    print version(ARGS.version)
else:
    APP_NAME = ARGS.app if ARGS.app else raw_input("Please Enter Your App Name: ")
    print macneed_search(APP_NAME)
