from models import Trick
from bs4 import BeautifulSoup
import requests
import json
from loguru import logger

class Scraper():
    url = ''
    base_url = ''
    query = ""
    max_page = None
    login_timeout = 240
    retries = 3
    platform = ''

    def save(self, link, title, description):
        try:
            Trick.insert(platform=self.platform, title=title, link=link, content=description).execute()
        except Exception as e:
            logger.info(e)


