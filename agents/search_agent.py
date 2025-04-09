import requests
from bs4 import BeautifulSoup

class SearchAgent:
    def __init__(self):
        self.base_url = "https://scholar.google.com/scholar"

    def search_papers(self, query, num_results=5):
        params = {"q": query, "num": num_results}
        response = requests.get(self.base_url, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for item in soup.select(".gs_ri"):
            title = item.select_one(".gs_rt").get_text()
            link = item.select_one("a")["href"]
            snippet = item.select_one(".gs_rs").get_text()
            results.append({"title": title, "link": link, "snippet": snippet})
        return results