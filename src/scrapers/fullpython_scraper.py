from bs4 import BeautifulSoup
import requests
from loguru import logger
from basescrapers import Scraper

class FullStackPythonScraper(Scraper):
    url = 'https://www.fullstackpython.com/blog.html'
    base_url = 'https://www.fullstackpython.com/'
    query = ""
    max_page = 1
    platform = 'FullStackPython'

    def run(self):
        html_content = requests.get(self.url).text
        page = BeautifulSoup(html_content, 'lxml')
        logger.info(self.url)

        bloc = page.find('div', attrs={'class':'cn'})
        trick_list = bloc.find_all('div', attrs={'class':'row'})
        print(len(trick_list))
        for trick in trick_list:
            try:
                title = trick.find('h2').text
                logger.debug(f'Title is {title}')
                detail_link = self.base_url + trick.find('a').get('href')

                desc = trick.find('p').text
                self.save(title, detail_link, desc)
            except AttributeError:
                pass
           

if __name__=='__main__':
    scraper = FullStackPythonScraper()
    scraper.run()