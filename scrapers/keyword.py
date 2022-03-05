import requests
from bs4 import BeautifulSoup
from utils import URLFormatter, headers, proxies


class KeywordScraper:

    def __init__(self, query):
        self.requests = requests.Session()
        self.query = query
        self.raw_html = BeautifulSoup("", "html.parser")
        self.access_SERP()
        self.scrape_question()
        self.scrape_related_searches()
    def access_SERP(self):
        url = URLFormatter(self.query).final_url()
        try:
            request = self.requests.get(url, headers=headers, proxies=proxies)
        except requests.exceptions.RequestException:
            raise requests.exceptions.ConnectionError("Are you Sure you are Connected to the Internet")
        if request.status_code == 200:
            self.raw_html = BeautifulSoup(request.content, "html.parser")
        else:
            raise requests.exceptions.ConnectionError("Connection Blocked By Google")

    def scrape_question(self):
        question_container = self.raw_html.find("div", {"class": ["AuVD","cUnQKe"]})
        if question_container is not None:
            questions = question_container.find_all("div", {"class": ["wQiwMc", "ygGdYd", "related-question-pair"]})
            for question in questions:
                i = question.find("span").text
        else:
            pass

    def scrape_related_searches(self):
        related_searches_divs = self.raw_html.find_all("div", {"class": "AJLUJb"})
        if related_searches_divs:
            for div in related_searches_divs:
                questions = div.find_all("a", {"class": ["k8XOCe", "R0xfCb", "VCOFK","s8bAkb"]})
                for question in questions:
                    i = question.find("div", {"class": ["s75CSd", "OhScic","AB4Wff"]}).text

    def scrape_auto_complete(self):
        pass
