

class URLFormatter:

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = "https://google.com/search?q="
        self.formatted_keyword = ""
        self.format_keyword()

    def format_keyword(self):
        keyword_list = self.keyword.split()
        formatted = "" + keyword_list[0]
        for i in keyword_list[1:]:
            formatted = formatted + "+" + i
        self.formatted_keyword = formatted

    def final_url(self):
        return self.url + self.formatted_keyword


headers = {

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "www.google.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
    "Accept-Language": "en-us",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive"
}
proxies = {
    "http": ""
}