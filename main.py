#!/usr/bin/python
# - coding: utf-8 -*-
import os
import sys
import json
import argparse
from urllib.request import urlopen
from urllib.parse import parse_qs
from bs4 import BeautifulSoup

def store_list_to_json(token):
    rt={}
    rt["name"]=token.find(class_="font120").get_text().replace("\u3000"," ")
    rt["map_url"]=token.find("a").get("href")
    rt["address"]=token.select_one("th:has(span:contains('住所')) ~ td").get_text().split("\n")[0].replace("\u3000"," ")
    rt["TEL"]=token.select_one("th:has(span:contains('電話番号')) ~ td").get_text()
    rt["area"]=token.select_one("th:has(span:contains('エリア')) ~ td").get_text()
    rt["genre"]=token.select_one("th:has(span:contains('料理ジャンル')) ~ td").get_text()
    return rt


def get_store_list(url, mode, page):
    f=urlopen(url+"?mode={mode}&p={page}".format(mode=mode,page=page))
    return f

def parse_store_list(html):
    soup=BeautifulSoup(html,"html.parser")
    next_page_link=soup.find(class_="nextpostslink")
    if next_page_link == None:
        return None, None
    next_page=next_page_link.get('href')
    query_string=parse_qs(next_page)
    next_page_number=max([ int(x) for x in query_string['p']])
    store_list=soup.find_all(class_="store-list")

    store_list_json=[]
    for store in store_list:
        store_list_json.append(store_list_to_json(store))

    return next_page_number, store_list_json

def read_all():
    url=os.environ['BASE_URL']
    page=1
    json_store_list=[]
    while page != None:
        page, tmp = parse_store_list(get_store_list(url,"all",page))
        if tmp != None:
            json_store_list.extend(tmp)
    return json_store_list

if __name__ == "__main__":
    if "BASE_URL" not in  os.environ:
        print("you have to set environment variable 'BASE_URL'", file=sys.stderr)
        exit(1)
    parser = argparse.ArgumentParser(description="get all store list from KAGAWA go to eat campaign")
    parser.add_argument("-i","--indent", dest="indent", help="indent level")
    args=parser.parse_args()
    indent=int(args.indent) if args.indent is not None else None
    json.dump(read_all(),sys.stdout,ensure_ascii=False,indent=indent)
