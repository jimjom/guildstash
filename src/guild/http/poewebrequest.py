import requests
import os
import pickle
import time as timet
from datetime import *
from dotenv import load_dotenv



class PoEWebRequest:

    __poessid__ = ''

    __headers__ = ''

    __result__ = None

    def __init__(self):
        load_dotenv()
        
        self.__poessid__ = os.getenv('POESESSID')
        self.__headers__ = {
            "POESESSID": self.__poessid__
        }

    def makeRequest(self, url):
        s = requests.session()

        s.cookies.set("POESESSID", self.__poessid__)
        s.cookies.set("cf_clearance", "BG6MtZG73rTNDCHB4CaJ2wCt5RlkjQSd7WY4cvyg_mA")
        s.cookies.set("stored_data", "1")
        s.cookies.set("_ga", "GA1.2.1716915880.1629409194")
        s.cookies.set("_gid", "GA1.2.92074025.1673491042")

        header = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "path": "api/trade/search/Sanctum",
            "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76",
            "x-requested-with": "XMLHttpRequest",
            "Referer": url,
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "POESESSID": self.__poessid__
        }

        s.headers.update(header)
        
        self.__result__ = s.get(url)

        if self.__result__.status_code != 200:
            print("Error %d:\n\t %s", self.__result__.status_code, self.__result__.content)
        
        return self.__result__
