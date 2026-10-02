import requests
from bs4 import BeautifulSoup

def get_soup(session, url):
    resp = session.get(url, timeout=10)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def main():
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (porco_de_ouro_automation)"})
    
    home_url = "https://palmeiras.com.br/home"
    home_html = get_soup(session, home_url)
    
    match_url = home_html.select_one("#masthead > div > div.container-top > div.faixa > div > div.header-tempo-real > div > a").get("href")
    
    match_html = get_soup(session, match_url)
    
    # home_team = match_html.select_one("#placar > div.mandante > span.jogo-time")
    
    print(match_html)

if __name__ == "__main__":
    main()