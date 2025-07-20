from lexicon import *

import json
import os

def cls(): os.system("clear")

def upload(file):
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(file, f, ensure_ascii=False, indent=4)

def read_js():
    global data

    with open("config.json", "r", encoding="utf-8") as f:
        data = json.load(f)

